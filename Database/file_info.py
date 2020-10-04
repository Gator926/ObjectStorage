import sqlite3


class FileInfo:
    def __init__(self):
        self.connect = sqlite3.connect("../ObjectStorage.db")

    def __del__(self):
        self.connect.close()

    def insert_file_info(self, local_path: str, remote_path: str, version_id: str, md5: str):
        """
        查询文件信息
        :param local_path:  本地文件路径
        :param remote_path: 远程文件路径
        :param version_id:  版本id
        :param md5:         文件md5
        """
        sql = f'INSERT INTO main.file_info (local_path, remote_path, version_id, md5) VALUES ("{local_path}", "{remote_path}", "{version_id}", "{md5}")'
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()

    def select_file_info_by_localpath_and_versionid(self, local_path: str, version_id: str):
        """
        根据local path和version id获取文件数据内容
        :param local_path:
        :param version_id:
        :return: 数据内容 (())
        """
        sql = f"SELECT * FROM file_info"
        cursor = self.connect.cursor()
        result = cursor.execute(sql)
        return result.description
