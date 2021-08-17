# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 19:28:57 2021

@author: bpapa
"""
import requests
#
def gooddata_login(domain, username, password):
    request = requests.post('https://' + domain + '/gdc/account/login'
                    ,headers = {'Accept':'application/json', 'Content-type':'application/json'}
                    ,json = {'postUserLogin':{"login": username, "password": password, "remember": 1}})
    return(request.headers)
#
def get_TT_token(domain, GDCAuthSST):
    request = requests.get('https://' + domain + '/gdc/account/token'
                    ,headers = {'Accept':'application/json', 'Content-type':'application/json', 'X-GDC-AuthSST': GDCAuthSST})
    return(request.text)
#
def gooddata_logout(domain, profile_id, GDCAuthTT):
    request = requests.delete('https://' + domain + '/gdc/account/login/' + profile_id
                    ,headers = {'Accept':'application/json', 'Content-type':'application/json'}
                    ,cookies = {'GDCAuthTT': GDCAuthTT})
    return(request.headers)
#   
def modify_authentication_settings_for_a_user(domain, profile_id, GDCAuthTT, first_name, last_name, sso_provider, autenticationModes):
    request = requests.put('https://' + domain + '/gdc/account/profile/' + profile_id
                    ,headers = {'Accept':'application/json', 'Content-type':'application/json'}
                    ,cookies = {'GDCAuthTT': GDCAuthTT}
                    ,json = {"accountSetting": { "firstName": first_name, "lastName": last_name, "ssoProvider": sso_provider, "authenticationModes": autenticationModes }}) 
    return(request)
#   
def check_platform_availability(domain):
    request = requests.get('https://' + domain + '/gdc/ping'
                    ,headers = {'Accept':'application/json', 'Content-type':'application/json'})
    return(request)
