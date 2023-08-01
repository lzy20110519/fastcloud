# 测试文件
import requests
import json
import hashlib
import os


class XesUploader:
    def uploadAbsolutePath(self, filepath):
        md5 = None
        contents = None
        if os.path.isfile(filepath):
            fp = open(filepath, 'rb')
            contents = fp.read()
            fp.close()
            md5 = hashlib.md5(contents).hexdigest()

        if md5 is None or contents is None:
            raise Exception("文件不存在")

        uploadParams = self._getUploadParams(filepath, md5)
        requests.request(method="PUT", url=uploadParams['host'], data=contents, headers=uploadParams['headers'])
        return uploadParams['url']

    def _getUploadParams(self, filename, md5):
        url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
        params = {"scene": "offline_python_assets", "md5": md5, "filename": filename}
        response = requests.get(url=url, params=params)
        data = json.loads(response.text)['data']
        return data


print('XESPan 版权无，翻印不究。但请协助改进本作品。')
print('本项目核心代码由 月光下的魔术师（ID:15789959）提供 本作作者不拥有该项目')
print(
    '参考：https://code.xueersi.com/home/project/detail?lang=code&pid=31919492&version=offline&form=python&langType=python')
print('本项目使用开源协议:UNLECENSE')
print('\n' * 3)
uploader = XesUploader()
while True:
    path = input('上传文件的绝对路径:')
    print('UPLOADING...')
    url = uploader.uploadAbsolutePath(path)
    print('上传成功！')
    print('文件地址:', url)
