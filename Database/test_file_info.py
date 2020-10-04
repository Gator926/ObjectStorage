from Database.file_info import FileInfo


class TestFileInfo:
    def setup(self) -> None:
        self.file_info = FileInfo()

    def teardown(self) -> None:
        self.file_info.__del__()

    def test_insert_file_info(self):
        self.file_info.insert_file_info("local_path1", "remote_path1", "version_id1", "md51")
        assert True

    def test_select_file_info(self):
        self.file_info.select_file_info_by_localpath_and_versionid("", "")