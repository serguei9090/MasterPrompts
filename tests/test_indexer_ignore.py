import unittest
import os
import sys
from pathlib import Path
import fnmatch

# Add the project root to sys.path so we can import indexer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.cognee.indexer import get_ignore_spec, get_filtered_files

class TestIndexerIgnore(unittest.TestCase):
    def setUp(self):
        self.spec = get_ignore_spec()

    def is_ignored(self, path):
        """Uses pathspec to check if a path should be ignored."""
        # Folders in pathspec rules usually need a trailing slash to match directory rules
        if not os.path.basename(path) and not path.endswith('/'):
            path += '/'
        return self.spec.match_file(path)

    def test_node_modules_ignored(self):
        """Confirm that various node_modules paths are correctly identified as ignored."""
        test_paths = [
            "node_modules/package/index.js",
            ".agents/skills/chrome-devtools/scripts/node_modules/@babel/code-frame/LICENSE",
            "src/components/node_modules/test.txt",
        ]
        
        for path in test_paths:
            with self.subTest(path=path):
                self.assertTrue(self.is_ignored(path), f"Path should be ignored: {path}")

    def test_valid_files_not_ignored(self):
        """Confirm that legitimate source files are NOT ignored."""
        valid_paths = [
            "scripts/cognee/indexer.py",
            "README.md",
            "src/app.js",
            ".agents/agents.md"
        ]
        
        for path in valid_paths:
            with self.subTest(path=path):
                self.assertFalse(self.is_ignored(path), f"Path should NOT be ignored: {path}")

if __name__ == "__main__":
    unittest.main()
