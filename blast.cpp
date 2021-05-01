//Graph building 
    //loop through lines of reads
        //for each line, store the L kmer and the R kmer (maybe in graph nodes directly?) - this would require edge building right there
            //edge building logic: 
            //use 225 directed graph code
            //note number of semi-balanced (indegree and outdegree are 1 apart) nodes and unbalanced (more than 1 apart) nodes
                //if any node has 0 indegree, output -1
//Graph Walking
    //if any unbalanced nodes, or if semi-unbalanced nodes # != 0 or 2, output -1
    //need to know how to perform eulerian walk - https://www.geeksforgeeks.org/euler-circuit-directed-graph/
    