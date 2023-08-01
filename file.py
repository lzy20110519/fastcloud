import hashlib
import json
import os
import time

import requests
from tqdm import tqdm


class Update(object):
    def calculate_md5(self, filepath):
        md5_hash = hashlib.md5()
        chunk_size = 20 * 1024 * 1024  # 20MB chunk size
        total_size = os.path.getsize(filepath)
        bytes_read = 0

        start_time = time.time()

        with open(filepath, 'rb') as file, tqdm(total=total_size, unit='B', unit_scale=True,
                                                desc='计算MD5进度') as pbar:
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                md5_hash.update(data)
                bytes_read += len(data)
                pbar.update(len(data))

                # 输出每个20MB数据块的MD5
                chunk_md5 = hashlib.md5(data).hexdigest()
                print(f"20MB 数据块的MD5哈希值: {chunk_md5}")

        md5_digest = md5_hash.hexdigest()
        print(f"\n整个文件的MD5 哈希值: {md5_digest}")
        return md5_digest

    def _getUploadParams(self, md5, filename):
        url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
        params = {"scene": "offline_python_assets", "md5": md5, "filename": filename}
        response = requests.get(url=url, params=params)
        data = json.loads(response.text)['data']
        return data

    @classmethod
    def update_file(cls, filepath):
        updater = cls()
        file_md5 = updater.calculate_md5(filepath)
        data = updater._getUploadParams(file_md5, os.path.basename(filepath))
        print(data)
        return data


