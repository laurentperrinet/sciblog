cd ../files/2014-11-10_balaV1-protocol/
rm -fr 2014-12-10_balaV1-protocol.zip 2014-12-10_balaV1
ipython3 2014-12-10_balaV1-protocol.py
zip 2014-12-10_balaV1-protocol.zip 2014-12-10_balaV1-protocol.* 2014-12-10_balaV1/* 2014-12-10_balaV1/**/*
rm -fr 2014-12-10_balaV1
cd ../../posts
echo 'done'
