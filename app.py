#!/usr/bin/python
# -*- coding: utf-8 -*-

#?                  References
#* ==================================================
# https://api.coursera.org/api/courses.v1?page=1&&limit=10242
# https://github.com/MrMoshkovitz/pycourses/blob/master/app.py
#* ==================================================
#?                  Coursera
#* ==================================================
# https://about.coursera.org/affiliates
# https://app.impact.com/signup/none/create-new-mediapartner-account-flow.ihtml?execution=e1s1#/?viewkey=signUpContractPreview
# https://app.impact.com/secure/member/home/mview.ihtml
# https://building.coursera.org/developer-program
# https://github.com/Forks-Scrappers/Coursera-Course-Dataset/
# https://colab.research.google.com/drive/1VUrzrnvtBcqlQ6OtaShGTbAuzlsttH9Z
# https://medium.com/coursera-engineering
# https://api.coursera.org/api/courses.v1?limit=52&fields=instructorIds,partnerIds,specializations,domainTypes,categories,description,workload,primaryLanguages,partnerLogo,photoUrl
# https://tech.coursera.org/app-platform/catalog
# https://build.coursera.org/app-platform/catalog/
# https://api.coursera.org/api/courses.v1
# "https://api.coursera.org/api/"
# https://api.coursera.org/api/courses.v1?page=1&&limit=10242
# https://www.coursera.org/directory

#?                  Web Imports
#* ==================================================
from flask import Flask, jsonify, request
app = Flask(__name__)
import requests
from json import loads, dumps


#?                  Local Files Import
#* ==================================================


#?                  Variables
#* ==================================================


#?                  Application Routes
#* ==================================================
#* ==================================================

#?                  Main Route
#* ==================================================

@app.route('/')
def index():
    return """<html>
    <head>
        <title>Course Digger
        </title>
    </head>
    <body>
    <p> particular course: -<br><br>
            url:- /course/api/v1.0/courses/course_name<br><br>
            <br><br>
    <p> particular course from a particular site: -<br><br>
            url:- /course/api/v1.0/courses/provider/course_name<br><br>
            <br><br>
    <p> To extract all courses from coursera: -<br><br>
            url:- /course/api/v1.0/courses/coursera?start="start results from this number"&limit="number of results to display on a page"<br><br>
            <br><br>
    <p> To extract details of all courses from udacity: -<br><br>
            url:- /course/api/v1.0/courses/udacity<br><br>
            <br><br>
    <p> To extract details of all courses from udemy: -<br><br>
            url:-  /course/api/v1.0/courses/udemy?pagesize="number of results to display on page"<br><br>
            <br><br>
        </body>
</html>"""


#?                  Coursera Routes
#* ==================================================
@app.route('/api/v1.0/courses/coursera', methods=['GET'])
def AllCourseFromCoursera():
    start = request.args.get('start')
    limit = request.args.get('limit')
    coursera = coursera_all_courses(start, limit)
    c={"courses":coursera}
    return c
    # return dumps(c,indent=4, sort_keys=True)








#?                  Course Diggers
#* ==================================================
#* ==================================================

#?                  Coursera Digger
#* ==================================================
def coursera_all_courses(start, limit):
    limit = loads(requests.get('https://api.coursera.org/api/courses.v1').text)['paging']['total']
    coursera_all_courses = []
    url_params = 'slug,courseType,primaryLanguages,description'

    url = 'https://api.coursera.org/api/courses.v1?limit=' + str(limit) + '&fields=' + url_params
    res = requests.get(url)
    results = res.text
    json_result = loads(results)
    for item in json_result['elements']:
        if 'en' in item['primaryLanguages']:
            coursera_all_courses.append(coursera_store_course(item))

    return coursera_all_courses


def coursera_store_course(item):
    name = item['name']
    type = item['courseType']
    slug = item['slug']

    if 'v2' in type:
        course_url = 'https://www.coursera.org/learn/' + slug
    else:
        course_url = 'https://www.coursera.org/course/' + slug

    description = item['description']
    course = {
        'name': name,
        'url': course_url,
        'description': description,
        'provider': 'coursera',
        'price': 'Null',
        }
    return course











if __name__ == '__main__':
   
    app.run(debug=True)

