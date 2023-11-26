def handling_fields(value_field, issue) -> str:
    list_default_values = ["issuekey", "assignee", "reporter", "resolution", "resolutiondate", "status", "updated",
                           "summary"]

    # Trata campos obrigatórios do JIRA
    if value_field in list_default_values:
        if value_field == "issuekey":
            return issue['key']
        if value_field == "assignee":
            return issue['fields']['assignee']['displayName']
        if value_field == "reporter":
            return issue['fields']['reporter']['displayName']
        if value_field == "resolution":
            return issue["fields"]["resolution"]["name"]
        if value_field == "resolutiondate":
            return issue["fields"]["resolutiondate"]
        if value_field == "summary":
            return issue["fields"]["summary"]
        if value_field == "status":
            return issue["fields"]["status"]["name"]

    # Trata custom_fields desconhecidos 
    if value_field in issue["fields"]:
        if issue['fields'][value_field] is None:
            return "-"
        elif isinstance(issue["fields"][value_field], str):
            return issue["fields"][value_field]
        elif isinstance(issue["fields"][value_field], dict):
            return issue["fields"][value_field]['value']
        elif isinstance(issue['fields'][value_field], list):
            if isinstance(issue["fields"][value_field][0], dict):
                return issue["fields"][value_field][0]["value"]
            else:
                concatenado = ",".join(issue['fields'][value_field])
                return concatenado
        elif isinstance(issue["fields"][value_field], float):
            return issue["fields"][value_field]


