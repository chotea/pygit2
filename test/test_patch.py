BLOB_OLD_SHA = 'a520c24d85fbfc815d385957eed41406ca5a860b'
BLOB_NEW_SHA = '3b18e512dba79e4c8300dd08aeb37f8e728b8dad'
BLOB_OLD_CONTENT = b"""hello world
"""
BLOB_PATCH2 = """diff --git a/a/file b/b/file
index a520c24..3b18e51 100644
--- a/a/file
+++ b/b/file
@@ -1,3 +1 @@
 hello world
-hola mundo
-bonjour le monde
"""

            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        old_blob = self.repo[BLOB_OLD_SHA]
        new_blob = self.repo[BLOB_NEW_SHA]
            old_blob,
            new_blob,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        self.assertEqual(patch.patch, BLOB_PATCH2)
        old_blob = self.repo[BLOB_OLD_SHA]
            old_blob,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,
        old_blob = self.repo[BLOB_OLD_SHA]
            old_blob,
            old_as_path=BLOB_OLD_PATH,
            new_as_path=BLOB_NEW_PATH,

    def test_patch_create_from_bad_old_type_arg(self):
        with self.assertRaises(TypeError):
            pygit2.Patch.create_from(
                self.repo,
                BLOB_NEW_CONTENT,
            )

    def test_patch_create_from_bad_new_type_arg(self):
        with self.assertRaises(TypeError):
            pygit2.Patch.create_from(
                None,
                self.repo,
            )