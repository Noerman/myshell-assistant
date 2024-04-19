# -*- coding: utf-8 -*-



# url = 'https://docs.myshell.ai'

url = 'https://developer.android.com/training/wearables/wff'



from bs4 import BeautifulSoup
import urllib.parse
import requests
import logging
import queue
import os
import re
from javascript import require
from typing import (
    List,
    Optional,
    Union
)

logger = logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s', datefmt='%H:%M:%S')

TurndownService = require('turndown')
turndownPluginGfm = require('turndown-plugin-gfm')

def url_to_folder_name(url):

    folder_name = re.sub(r"^(https?|ftp)://", "", url)

    folder_name = folder_name.replace(".", "-")

    return folder_name

base_dir = url_to_folder_name(url)

base_dir = f'docs\{base_dir}'

DEFAULT_BASE_DIR = f'./{base_dir}/'
DEFAULT_TARGET_CONTENT = ['main']
DEFAULT_TARGET_LINKS = ['body']


def turndown(input):
    gfm = turndownPluginGfm.gfm
    turndownService = TurndownService({
    'headingStyle': 'atx',
    'hr': '---',
    'bulletListMarker': '-',
    'codeBlockStyle': 'fenced'
    })

    turndownService.use(gfm)
    output = turndownService.turndown(input)
    return output

def conditional_replace(text):
    def replacer(match):

        content = match.group(1)
        link = match.group(2)

        if "https://" not in link:
            return ""
        else:
            return match.group(0)

    return re.sub(r'\[([^\]]*)\]\(([^)]*)\)', replacer, text)

def clean_text(text):

    text = conditional_replace(text)

    text = re.sub(r'(?<=# )\n{2,}', '', text)

    text = re.sub(r'(?<=## )\n{2,}', '', text)

    text = re.sub(r'(?<=### )\n{2,}', '', text)

    match = re.search(r"Last updated.*", text, flags=re.MULTILINE)
    if match:
        start, end = match.span()
        text = text[:start] + '' + text[end:]

    lines = text.splitlines()

    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()

    for i in range(len(lines) - 1, 0, -1):
        if not lines[i] and not lines[i - 1]:
            lines.pop(i)

    text = '\n'.join(lines)

    return text

def is_valid_url(url: str) -> bool:
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip('/'), None, None, None))

def get_file_paths(directory_path):

    file_paths = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_paths.append(full_path)
    return file_paths

def check_if_directory():
    file_paths = get_file_paths(f".\\{base_dir}")
    for file_path in file_paths:
        file_dir, filename = os.path.split(file_path)
        file_base, file_ext = os.path.splitext(filename)

        subdirectory_path = os.path.join(file_dir, file_base)
        if os.path.isdir(subdirectory_path):
            if os.path.exists(os.path.join(file_dir, '~' + filename)):
                os.remove(os.path.join(file_dir, '~' + filename))
            os.rename(file_path, os.path.join(file_dir, '~' + filename))
            print(f'📂 '+file_dir+'\~'+filename)
    return

def crawl(
    url: str,
    base_url: str,
    already_crawled: set,
    file_path: str,
    target_links: Union[str, List[str]] = DEFAULT_TARGET_LINKS,
    target_content: Union[str, List[str]] = None,
    valid_paths: Union[str, List[str]] = None,
    is_domain_match: Optional[bool] = True,
    is_base_path_match: Optional[bool] = False,
    is_links: Optional[bool] = True
) -> List[str]:

    if url in already_crawled:
        return []
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        return []
    if 'text/html' not in response.headers.get('Content-Type', ''):
        return []
    already_crawled.add(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Strip unwanted tags
    for element in soup(['script', 'style']):
        element.decompose()


    file_name = file_path.split("/")[-1]

    content = get_target_content(soup, target_content=target_content)

    if content:

        output = turndown(content)

        output = clean_text(output)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(output)

        print(f'🔃 {base_dir}\{file_name}')

    child_urls = get_target_links(
        soup,
        base_url,
        target_links,
        valid_paths=valid_paths,
        is_domain_match=is_domain_match,
        is_base_path_match=is_base_path_match    
    )

    return child_urls


def get_target_content(
    soup: BeautifulSoup,
    target_content: Union[List[str], None] = None
) -> str:

    content = ''

    if target_content:
        for target in target_content:
            for tag in soup.select(target):
                content += f'{str(tag)}'

    else:
        max_text_length = 0
        for tag in soup.find_all(DEFAULT_TARGET_CONTENT):
            text_length = len(tag.get_text())
            if text_length > max_text_length:
                max_text_length = text_length
                main_content = tag

        content = str(main_content)

    return content if len(content) > 0 else False

def get_target_links(
    soup: BeautifulSoup,
    base_url: str,
    target_links: List[str] = DEFAULT_TARGET_LINKS,
    valid_paths: Union[List[str], None] = None,
    is_domain_match: Optional[bool] = True,
    is_base_path_match: Optional[bool] = False
) -> List[str]:

    child_urls = []
    parsed_base_url = urllib.parse.urlparse(base_url)  

    for target in soup.find_all(target_links):
        for link in target.find_all('a'):
            child_url = urllib.parse.urljoin(base_url, link.get('href'))
            parsed_child_url = urllib.parse.urlparse(child_url)  
            
            if parsed_child_url.netloc == parsed_base_url.netloc: 
                child_urls.append(child_url)

    return child_urls 

q=queue.Queue()

def md_crawl(
        base_url: str,
        max_depth: Optional[int] = 24,
        base_dir: Optional[str] = DEFAULT_BASE_DIR,
        target_links: Union[str, List[str]] = DEFAULT_TARGET_LINKS,
        target_content: Union[str, List[str]] = None,
        valid_paths: Union[str, List[str]] = None,
        is_domain_match: Optional[bool] = True,
        is_base_path_match: Optional[bool] = False,
        is_debug: Optional[bool] = False,
        is_links: Optional[bool] = True
) -> None:
    if is_domain_match is False and is_base_path_match is True:
        raise ValueError('❌ Domain match must be True if base match is set to True')

    if isinstance(target_links, str):
        target_links = target_links.split(',') if ',' in target_links else [target_links]

    if isinstance(target_content, str):
        target_content = target_content.split(',') if ',' in target_content else [target_content]

    if isinstance(valid_paths, str):
        valid_paths = valid_paths.split(',') if ',' in valid_paths else [valid_paths]

    if not is_valid_url(base_url):
        raise ValueError('❌ Invalid base URL')

    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    already_crawled = set()

    q=queue.Queue()

    q.put((0, base_url))

    while not q.empty():
        depth, url = q.get()
        if depth > max_depth:
            continue

        parsed_url = urllib.parse.urlparse(url)
        path_components = parsed_url.path.strip("/").split("/")

        dir_path = base_dir
        for component in path_components[:-1]:
            dir_path = os.path.join(dir_path, component)

        os.makedirs(dir_path, exist_ok=True)

        file_name = 'introduction' if not path_components[-1] else path_components[-1]
        file_name = '-'.join(re.findall(r'\w+', file_name)) + ".md"

        file_path = os.path.join(dir_path, file_name)

        child_urls = crawl(
            url,
            base_url,
            already_crawled,
            file_path,
            target_links,
            target_content,
            valid_paths,
            is_domain_match,
            is_base_path_match,
            is_links
        )
        child_urls = [normalize_url(u) for u in child_urls]

        if child_urls:  
            for child_url in child_urls:
                q.put((depth + 1, child_url))

#        time.sleep(1) 

print(f'✨ Let\'s fetch some updates!')
while True:
        try:
            md_crawl(url)
            if q.empty():
                break
        except KeyboardInterrupt:
            break
check_if_directory()
print('✅ All done!')