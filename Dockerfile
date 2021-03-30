FROM python:3.8 as build_deps
EXPOSE 80
WORKDIR /var/oneid
RUN sed -i "s@http://deb.debian.org/debian@http://mirrors.aliyun.com/debian/@g" /etc/apt/sources.list &&\
    sed -i "s@http://security.debian.org/debian-security@http://mirrors.aliyun.com/debian-security@g" /etc/apt/sources.list &&\
    apt-get update &&\
    apt-get install -y --no-install-recommends \
        gettext xmlsec1 \
        python-dev default-libmysqlclient-dev tini
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# FROM build_deps as run_lint
# ADD requirements-dev.txt ./
# RUN pip install --no-cache-dir -r requirements-dev.txt -i https://mirrors.aliyun.com/pypi/simple/
# ADD . .
# ARG base_commit_id=""
# RUN pre-commit install \
#     && make BASE_COMMIT_ID=${base_commit_id} lint

# FROM build_deps as run_test
# ADD . .
# RUN make test
# RUN python manage.py migrate && python manage.py test siteapi.v1.tests infrastructure.tests.test_file infrastructure.tests.test_sms --settings=oneid.settings_test

FROM build_deps as build
RUN pip install mysqlclient==1.4.6 -i https://mirrors.aliyun.com/pypi/simple/
ADD . .
RUN python manage.py compilemessages
ENTRYPOINT ["tini", "--"]
CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:80