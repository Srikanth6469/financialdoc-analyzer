## tasks.py

from crewai import Task
from agents import financial_analyst, verifier
from tools import search_tool, FinancialDocumentTool, InvestmentTool, RiskTool

# Instantiate tool objects
financial_doc_tool = FinancialDocumentTool()
investment_tool = InvestmentTool()
risk_tool = RiskTool()

# ---------------- Task 1: Analyze Financial Document ----------------
analyze_financial_document = Task(
    description="Analyze the user's query: {query} and provide financial insights.\n"
                "Use the financial document reader tool to extract insights.\n"
                "Optionally, search the internet for related data.",
    expected_output="Provide a detailed financial analysis.\n"
                    "Highlight market risks and investment opportunities.\n"
                    "Include relevant URLs for credibility.",
    agent=financial_analyst,
    tools=[financial_doc_tool, search_tool],
    async_execution=False,
)

# ---------------- Task 2: Investment Analysis ----------------
investment_analysis = Task(
    description="Perform investment analysis on the financial data.\n"
                "Provide stock/crypto/product recommendations based on insights.\n"
                "User asked: {query}, but feel free to expand with general market trends.",
    expected_output="List at least 10 investment recommendations with rationale.\n"
                    "Include market research, financial ratios, and risk factors.",
    agent=financial_analyst,
    tools=[financial_doc_tool, investment_tool],
    async_execution=False,
)

# ---------------- Task 3: Risk Assessment ----------------
risk_assessment = Task(
    description="Perform risk assessment based on financial document data.\n"
                "Highlight possible risks, market volatility, and external threats.",
    expected_output="Provide a structured risk assessment report.\n"
                    "- Market risks\n"
                    "- Credit risks\n"
                    "- Operational risks\n"
                    "- Speculative risks\n"
                    "Include recommendations for mitigation.",
    agent=financial_analyst,
    tools=[financial_doc_tool, risk_tool],
    async_execution=False,
)

# ---------------- Task 4: Verification ----------------
verification = Task(
    description="Verify if the uploaded file is a financial document.\n"
                "Classify the type of document and its relevance.",
    expected_output="State whether the file is a financial document.\n"
                    "Provide reasoning and possible use cases.\n"
                    "Add the detected file path.",
    agent=verifier,
    tools=[financial_doc_tool],
    async_execution=False,
)
