from ENGINEERING.MEMORY.memory_engine import runtime_memory


print()
print("==============================================")
print("BRAHMA Memory Update Test")
print("==============================================")
print()

memories = runtime_memory.recall_long_term()

if not memories:
    print("No long-term memories found.")
    raise SystemExit

record = memories[0]

print("Before Update")
print("----------------------------------------------")
print("UID        :", record.uid)
print("Content    :", record.content)
print("Importance :", record.importance)
print()

record.content = record.content + " [UPDATED]"
record.importance = record.importance + 0.1

updated = runtime_memory.update_memory(record)

if updated is None:
    print("Memory update failed.")
    raise SystemExit(1)

print("After Update")
print("----------------------------------------------")
print("UID        :", updated.uid)
print("Content    :", updated.content)
print("Importance :", updated.importance)
print()

print("Memory update completed successfully.")
print()