AZURE_EMAIL_CONNECTION_STRING_SERVER_LINK= https://portal.azure.com/#@nexsysit.co.in/resource/subscriptions/db664da8-36f8-4d9e-9fd2-df37767980da/resourceGroups/InsurancePRG/providers/Microsoft.Communication/CommunicationServices/insurance-communication-service/resource_overview
AZURE_SENDER_EMAIL_SERVER_LINK= https://portal.azure.com/#@nexsysit.co.in/resource/subscriptions/db664da8-36f8-4d9e-9fd2-df37767980da/resourceGroups/InsurancePRG/providers/Microsoft.Communication/emailServices/Insurance-email-service/domains/AzureManagedDomain/emailServices_mailFromAddressesItem

main.py      → defines FastAPI app
run.py       → development runner (Windows fix)
uvicorn cmd  → production runner


python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

playwright install chromium

# Runs only when there is any change in table
alembic revision --autogenerate -m "initial"


# Run it every time
alembic upgrade head

python run.py

