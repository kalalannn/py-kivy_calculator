
echo "Profiling -C"
seq 1 10 | time ./cprof
echo ""
seq 1 100 | time ./cprof
echo ""
seq 1 1000 | time ./cprof
echo ""
seq 1 10000 | time ./cprof
echo ""
seq 1 100000 | time ./cprof
echo ""
seq 1 1000000 | time ./cprof
echo ""
seq 1 10000000 | time ./cprof
echo ""
seq 1 100000000 | time ./cprof

exit 1
echo "Profiling -Python"
seq 1 10 | time python3 profiling.py
echo ""
seq 1 100 | time python3 profiling.py
echo ""
seq 1 1000 | time python3 profiling.py
echo ""
seq 1 10000 | time python3 profiling.py
echo ""
seq 1 100000 | time python3 profiling.py
echo ""
seq 1 1000000 | time python3 profiling.py
echo ""
seq 1 10000000 | time python3 profiling.py
echo ""
seq 1 100000000 | time python3 profiling.py
