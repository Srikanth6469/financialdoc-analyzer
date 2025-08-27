## tools.py

import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader
# from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

## Creating search tool
search_tool = SerperDevTool()

# ---------------- Custom PDF Reader Tool ----------------
class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = "Reads and extracts content from financial PDF documents."

    def _run(self, path: str = "data/sample.pdf") -> str:
        """Reads financial data from a PDF file and returns cleaned text."""
        try:
            docs = PyPDFLoader(file_path=path).load()
            full_report = ""
            for data in docs:
                content = data.page_content

                # Remove extra whitespaces
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")

                full_report += content + "\n"

            return full_report.strip()
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

# ---------------- Investment Analysis Tool ----------------
class InvestmentTool(BaseTool):
    name: str = "Investment Analysis Tool"
    description: str = "Analyzes financial documents for investment opportunities."

    def _run(self, financial_document_data: str) -> str:
        # Placeholder implementation
        processed_data = financial_document_data.replace("  ", " ")

        # TODO: Replace with real analysis logic
        return "Investment analysis functionality to be implemented."

# ---------------- Risk Assessment Tool ----------------
class RiskTool(BaseTool):
    name: str = "Risk Assessment Tool"
    description: str = "Performs risk assessment on financial documents."

    def _run(self, financial_document_data: str) -> str:
        # TODO: Replace with real risk assessment
        return "Risk assessment functionality to be implemented."
