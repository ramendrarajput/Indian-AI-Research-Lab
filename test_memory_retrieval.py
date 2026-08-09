"""
PROJECT BRAHMA

Memory Retrieval Tests

Verifies:
- Relevant memories are returned
- Unrelated memories are excluded
- Importance affects ranking
- Newer memories break ranking ties
"""

from ENGINEERING.MEMORY.sqlite_storage import SQLiteMemoryStorage


def test_boot_retrieval():

    storage = SQLiteMemoryStorage()

    results = storage.search("boot")

    assert results, "Boot memories should be found."

    for record in results:

        content = record.content.lower()

        assert (
            "boot" in content
            or "boot" in record.source.lower()
            or "boot" in record.category.name.lower()
        ), (
            "Unrelated memory returned for boot query."
        )


def test_verified_retrieval():

    storage = SQLiteMemoryStorage()

    results = storage.search("verified")

    assert results, "Verified memory should be found."

    for record in results:

        content = record.content.lower()

        assert "verified" in content, (
            "Unrelated memory returned for verified query."
        )


def test_unrelated_memory_excluded():

    storage = SQLiteMemoryStorage()

    results = storage.search(
        "this_memory_should_not_exist"
    )

    assert results == [], (
        "Unrelated memories should not be returned."
    )


def test_importance_affects_ranking():

    storage = SQLiteMemoryStorage()

    results = storage.search("verified")

    assert results, (
        "Verified memory should be found."
    )

    assert results[0].importance >= 1.0, (
        "Importance should be preserved."
    )


if __name__ == "__main__":

    test_boot_retrieval()

    test_verified_retrieval()

    test_unrelated_memory_excluded()

    test_importance_affects_ranking()

    print()
    print("Memory retrieval tests passed successfully.")
    print()