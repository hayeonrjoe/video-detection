import requests
from bs4 import BeautifulSoup
import json
import logging
from app import app

app.logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
app.logger.addHandler(handler)


def detect_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        app.logger.error(f"Error fetching URL: {e}")
        return None

    print(f"URL {url} successfully fetched")
    app.logger.info(f"URL {url} successfully fetched")

    soup = BeautifulSoup(response.content, 'html.parser')

    video_tag = soup.find('video')
    mp4_urls = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.mp4')]
    json_ld_script = soup.find('script', type='application/ld+json')
    iframe_tags = soup.find_all('iframe')

    check_video_tag(video_tag)
    check_mp4_urls(mp4_urls)
    check_iframe_tags(iframe_tags)
    check_json_ld_script(json_ld_script)
    check_js_for_video(response.text)


def check_video_tag(video_tag):
    if video_tag:
        print("Video tag found.")
        app.logger.info("Video tag found.")
    else:
        print("No video tag found.")
        app.logger.info("No video tag found.")


def check_mp4_urls(mp4_urls):
    if mp4_urls:
        print("MP4 URLs found:", mp4_urls)
        app.logger.info(f"MP4 URLs found: {mp4_urls}")
    else:
        print("No MP4 URLs found.")
        app.logger.info("No MP4 URLs found.")


def check_iframe_tags(iframe_tags):
    if iframe_tags:
        for iframe_tag in iframe_tags:
            print("iframe tag found.")
            app.logger.info("iframe tag found.")
            iframe_src = iframe_tag.get('src')
            if iframe_src:
                if 'youtube.com' in iframe_src:
                    print("YouTube video detected in iframe.")
                    app.logger.info("YouTube video detected in iframe.")
    else:
        print("No iframe tags found.")
        app.logger.info("No iframe tags found.")


def check_json_ld_script(json_ld_script):
    if json_ld_script:
        print("JSON-LD script found. Parsing...")
        app.logger.info("JSON-LD script found. Parsing...")
        try:
            json_ld_data = json.loads(json_ld_script.string)
            if '@type' in json_ld_data and json_ld_data['@type'] == 'VideoObject':
                print("VideoObject found in JSON-LD script.")
                app.logger.info("VideoObject found in JSON-LD script.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            app.logger.error(f"Error decoding JSON: {e}")
    else:
        print("No JSON-LD script found.")
        app.logger.info("No JSON-LD script found.")


def check_js_for_video(js_code):
    if 'video' in js_code:
        print("JavaScript code contains references to video.")
        app.logger.info("JavaScript code contains references to video.")
    else:
        print("No video references found in JavaScript code.")
        app.logger.info("No video references found in JavaScript code.")
