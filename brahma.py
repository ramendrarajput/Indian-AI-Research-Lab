"""
══════════════════════════════════════════════════════════════

                PROJECT BRAHMA

        Universal Intelligence Architecture

        Powered by Indian AI Research Lab

══════════════════════════════════════════════════════════════

Author
------
Ramendra Singh Rajput

Description
-----------
Official Runtime Entry Point of Project BRAHMA.

This file is responsible for starting the Universal Runtime.

It intentionally contains almost no business logic.

Architecture

brahma.py
        ↓
startup.py
        ↓
boot.py
        ↓
kernel.py
        ↓
Universal Runtime

"""

from __future__ import annotations

import platform
import sys

from ENGINEERING.CORE.RUNTIME.startup import (
    runtime_health,
    startup_runtime,
)


# ==========================================================
# Banner
# ==========================================================

def print_banner():

    print()

    print("══════════════════════════════════════════════════════════════")
    print()
    print("                 🕉 PROJECT BRAHMA")
    print()
    print("         Universal Intelligence Architecture")
    print()
    print("          Powered by Indian AI Research Lab")
    print()
    print("══════════════════════════════════════════════════════════════")
    print()

    print("Version       : v0.2")

    print("Runtime       : Universal Runtime")

    print("Architecture  : BRAHMA")

    print(f"Python        : {platform.python_version()}")

    print(f"Platform      : {platform.system()}")

    print()


# ==========================================================
# Runtime Information
# ==========================================================

def print_runtime_status():

    health = runtime_health()

    runtime_info = health["runtime_summary"]

    kernel_info = health["kernel_summary"]

    print()

    print("────────────────────────────────────────────")

    print("Runtime Status")

    print("────────────────────────────────────────────")

    print()

    print(f"Kernel        : {kernel_info['kernel']}")

    print(f"Runtime       : {runtime_info['state']}")

    print(f"Version       : {runtime_info['version']}")

    print()

    print("Registered Services")

    for service in runtime_info["services"]:

        print(f"  ✓ {service}")

    print()

    print("────────────────────────────────────────────")

    print()


# ==========================================================
# Welcome
# ==========================================================

def print_welcome():

    print()

    print("Welcome to Project BRAHMA")

    print()

    print('"The birthplace of an idea does not determine"')

    print('"its destiny."')

    print()

    print('"Its architecture does."')

    print()

    print("Runtime Ready.")

    print()

    print("Future")

    print("------")

    print("• Universal Agent")

    print("• Scientific Laboratories")

    print("• Cognitive Runtime")

    print("• Artificial Intelligence")

    print("• Universal Intelligence")

    print()

    print("Type Ctrl+C to shutdown.")

    print()


# ==========================================================
# Main
# ==========================================================

def main():

    print_banner()

    startup_runtime()

    print_runtime_status()

    print_welcome()

    #
    # Future
    #
    # Universal Console
    #
    # >
    #
    # ChatGPT Runtime
    #
    # GUI Runtime
    #
    #

    while True:

        try:

            command = input("BRAHMA > ")

            if command.strip().lower() in {

                "exit",

                "quit",

            }:

                print()

                print("Shutting down Project BRAHMA...")

                break

            if command.strip() == "":

                continue

            print(f'Unknown command "{command}"')

            print("Runtime Console coming in v0.3")

        except KeyboardInterrupt:

            print()

            print()

            print("Runtime Interrupted.")

            break

    print()

    print("Goodbye.")

    print()


# ==========================================================

if __name__ == "__main__":

    try:

        main()

    except Exception as ex:

        print()

        print("BRAHMA Runtime Failed")

        print()

        print(ex)

        sys.exit(1)