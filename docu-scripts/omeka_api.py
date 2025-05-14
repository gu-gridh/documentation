from omeka_s_tools.api import OmekaAPIClient
import os
from dotenv import load_dotenv
# Load environment variables from .env file


def fetch_code_repos(omeka_auth):
    '''
    Get a list of code repositories from Omeka-S.
    Returns a list with code repos for each project:
    [{'heading': <project_label>, 
      'links': [
         {'link':  <repo_link>,
          'label': <repo_label>
          }
      ]
    }]
    '''
    res = []
    items = omeka_auth.filter_items_by_property(filter_property='schema:codeRepository', filter_type='ex')

    # TODO: Maybe fetch shortDescription from project item 
    for item in items['results']:
        if item['o:is_public']:
            project = {'heading': '',
                       'links': []}
            repos = item['schema:codeRepository']
            project_label = item['o:title']
            project['heading'] = project_label
            for repo in repos:
                if repo['is_public']:
                    if 'o:label' in repo:
                        repo_label = repo['o:label']
                    repo_link = repo['@id']
                    project['links'].append({'link': repo_link, 'label': repo_label})
            res.append(project)
    # sort alphabetically by project label
    sorted_res = sorted(res, key=lambda d: d['heading'])
    return sorted_res
    

def create_markdown(items):
    '''
    Build a markdown string with headings and links from results
    '''
    res = ''
    for item in items:
        heading = item['heading']     
        parts = []   
        for i in item['links']:
            parts.append("[" + i['label'] + "](" + i['link'] + ")")
        res += "### " + heading + "\n" + " | ".join(parts) + "\n"
    return res


def main():
    omeka_auth = OmekaAPIClient(os.getenv('API_URL_IDUN'),
                           key_identity=os.getenv('KEY_IDENTITY_IDUN'),
                           key_credential=os.getenv('KEY_CREDENTIAL_IDUN'),
                           apache_user=os.getenv('APACHE_USER_DEV'),
                           apache_pass=os.getenv('APACHE_PASS_DEV'))
    repos = fetch_code_repos(omeka_auth)
    repos_str = create_markdown(repos)
    print(repos_str)


if __name__ == "__main__":
    load_dotenv()
    main()
