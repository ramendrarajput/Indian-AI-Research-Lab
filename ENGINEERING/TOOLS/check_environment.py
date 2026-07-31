import sys

print("=" * 60)
print("Python Executable:")
print(sys.executable)
print("=" * 60)

"""
Project BRAHMA
Environment Checker

Author : Ramendra Singh Rajput
"""

import importlib


print("=" * 60)
print("        PROJECT BRAHMA ENVIRONMENT CHECKER")
print("=" * 60)

packages = [
    "streamlit",
    "google.generativeai",
    "google.cloud.texttospeech",
    "dotenv",
    "PyPDF2",
    "cv2",
    "pygame",
    "gtts",
    "speech_recognition",
    "langchain",
    "langchain_community",
    "langchain_google_genai",
    "langgraph",
    "faiss",
    "torch",
    "transformers",
    "diffusers",
    "phi",
    "crewai",
    "openai",
    "groq",
    "yfinance",
    "duckduckgo_search",
    "exa_py",
]

passed = 0
failed = 0

for package in packages:

    try:
        importlib.import_module(package)
        print(f"✅ {package}")

        passed += 1

    except Exception as e:

        print(f"❌ {package}")
        print(f"    {e}")

        failed += 1


print("=" * 60)

print(f"Passed : {passed}")

print(f"Failed : {failed}")

print("=" * 60)