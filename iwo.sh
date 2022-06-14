#!/bin/bash

function tweets {
    zless /net/corpora/twitter2/Tweets/2019/12/*.out.gz | \
    /net/corpora/twitter2/tools/tweet2tab -i date text | \
    egrep -v '^\s+' > n12.txt
    for month in 01 02 03 04 05 06
        do zless /net/corpora/twitter2/Tweets/2020/$month/*.out.gz | \
        /net/corpora/twitter2/tools/tweet2tab -i date text | \
        egrep -v '^\s+' > n$month\.txt
    done
}

tweets
echo done