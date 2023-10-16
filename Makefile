vXXX:
	make -C vXXX

v1:
	make -C v1

v21:
	make -C v21

v48:
	make -C v48

v53:
	make -C v53

v64:
	make -C v64

v103:
	make -C v103

v107:
	make -C v107

v203:
	make -C v203

v204:
	make -C v204

v302:
	make -C v302

v303:
	make -C v303

v353:
	make -C v353

v354:
	make -C v354

v400:
	make -C v400

v401:
	make -C v401

v500:
	make -C v500

v503:
	make -C v503

v601:
	make -C v601

v602:
	make -C v602

v606:
	make -C v606

v702:
	make -C v702

v704:
	make -C v704

vUS1:
	make -C vUS1

vUS2:
	make -C vUS2

vUS3:
	make -C vUS3

cXXX:
	make -C vXXX clean

c1:
	make -C v1 clean

c21:
	make -C v21 clean

c48:
	make -C v48 clean

c53:
	make -C v53 clean

c64:
	make -C v64 clean

c103:
	make -C v103 clean

c107:
	make -C v107 clean

c203:
	make -C v203 clean

c204:
	make -C v204 clean

c302:
	make -C v302 clean

c303:
	make -C v303 clean

c353:
	make -C v353 clean

c354:
	make -C v354 clean

c400:
	make -C v400 clean

c401:
	make -C v401 clean

c500:
	make -C v500 clean

c503:
	make -C v503 clean

c601:
	make -C v601 clean

c602:
	make -C v602 clean

c606:
	make -C v606 clean

c702:
	make -C v702 clean

c704:
	make -C v704 clean

cUS1:
	make -C vUS1 clean

cUS2:
	make -C vUS2 clean

cUS3:
	make -C vUS3 clean

all:
	make vXXX
	make v1
	make v21
	make v48
	make v53
	make v64
	make v103
	make v107
	make v203
	make v204
	make v302
	make v303
	make v353
	make v354
	make v400
	make v401
	make v500
	make v503
	make v601
	make v602
	make v606
	make v702
	make v704
	make vUS1
	make vUS2
	make vUS3

clean:
	make cXXX
	make c1
	make c21
	make c48
	make c53
	make c64
	make c103
	make c107
	make c203
	make c204
	make c302
	make c303
	make c353
	make c354
	make c400
	make c401
	make c500
	make c503
	make c601
	make c602
	make c606
	make c702
	make c704
	make cUS1
	make cUS2
	make cUS3

.PHONY: vXXX cXXX v1 c1 v21 c21 v48 c48 v53 c53 v64 c64 v103 c103 v107 c107 v203 c203 v204 c204 v302 c302 v303 c303 v353 c353 v354 c354 v400 c400 v401 c401 v500 c500 v503 c503 v601 c601 v602 c602 v702 c702 v704 c704 vUS1 cUS1 vUS2 cUS2 vUS3 cUS3 v606 c606 clean
