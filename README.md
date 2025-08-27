# Financial Document Analyzer - Debug Assignment
## Before Debugging (Issues Found)

1.LLM Initialization Error – TypeError: LLM.__init__() missing 1 required positional argument
2.Model Not Provided – API returned:
3.litellm.BadRequestError: LLM Provider NOT provided
4.File Path Issues – PDF not found (uploads/sample.pdf vs data/sample.pdf)
5.500 Internal Server Error – API crashed with unhandled exceptions
6.Agents Not Connected – financial_analyst agent not properly bound to tasks
7.PDF Parsing Bug – empty text returned for some PDFs
8.Unstructured API Response – JSON output was inconsistent and unclear

## After Debugging (Fixes Applied)
1.LLM Fixed – Implemented CrewAIDummyLLM with proper constructor
2.Provider Resolved – Added provider="gemini" and model for local testing
3.Correct File Handling – Standardized data/sample.pdf location
4.API Stability – Wrapped pipeline in try/except to avoid 500 errors
5.Agent-Task Linking – Tasks defined in tasks.py now properly call agents.py
6.Robust PDF Reader – Added fallback for empty pages, improved text extraction
7.Clean JSON Response




## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.


## Getting Started

### Install Required Libraries
```sh
pip install -r requirement.txt
```

### Sample Document
The system analyzes financial documents like Tesla's Q2 2025 financial update.

**To add Tesla's financial document:**
1. Download the Tesla Q2 2025 update from: https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf
2. Save it as `data/sample.pdf` in the project directory
3. Or upload any financial PDF through the API endpoint

**Note:** Current `data/sample.pdf` is a placeholder - replace with actual Tesla financial document for proper testing.

# You're All Not Set!
🐛 **Debug Mode Activated!** The project has bugs waiting to be squashed - your mission is to fix them and bring it to life.

## Debugging Instructions

1. **Identify the Bug**: Carefully read the code in each file and understand the expected behavior. There is a bug in each line of code. So be careful.
2. **Fix the Bug**: Implement the necessary changes to fix the bug.
3. **Test the Fix**: Run the project and verify that the bug is resolved.
4. **Repeat**: Continue this process until all bugs are fixed.

## Expected Features
- Upload financial documents (PDF format)
- AI-powered financial analysis
- Investment recommendations
- Risk assessment
- Market insights



# financialdoc-analyzer
