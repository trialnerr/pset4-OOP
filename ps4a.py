# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    collector_list = []
    if len(sequence) <= 1: 
       return sequence
    else: 
       for i in range(len(sequence)): # here you choose the element 
            x = sequence[i] 
            for p in get_permutations(sequence[:i] + sequence[i+1:]): # here you take it out to build all "subpermutations"
                collector_list.append(x + p) # here you add the chosen element again
                
       return collector_list

if __name__ == '__main__':
#   EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    # Put three example test cases here (for your sanity, limit your inputs
    #to be three characters or fewer as you will have n! permutations for a 
    #sequence of length n)

    example_input = '45'
    print('Input:', example_input)
    print('Expected Output:', ['45', '54'])
    print('Actual Output:', get_permutations(example_input))

    