echo "Profiling"
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
