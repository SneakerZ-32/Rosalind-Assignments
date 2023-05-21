 # Rosalind  -iprb-  Problem : Mendel's First Law
'''
from typing import Counter


dataset = [2,2,2] #input here your set

                               

    
kgen_pop = dataset[0] # Genotype: AA     | #populations by Genotype  
mgen_pop = dataset[1] # Genotype: Aa     |
ngen_pop = dataset[2] # Genotype: aa     |

gen_typ = len(dataset) #how many genotypes
tot_pop = 0 

for i in dataset:
    tot_pop += float(i)  # Your Total Population

# Possible Outcomes and Pr_of_desired Outcome(Phenotype of A):
Fixed_Pr ={'AA*AA':1, 'AA*Aa':1, 'AA*aa':0.5, 'Aa*AA':1, 'Aa*Aa':1, 'Aa*aa':0.75, 'aa*AA':0.5, 'aa*Aa':0.75, 'aa*aa':0}

def Pr_parent_1(*gen_pop): # Probability of Parent 1 being of that Genotype
    for gen in gen_pop:
        
    prob = gen_pop/tot_pop
    return prob 
print(Pr_parent_1(kgen_pop))

def Pr_parent_2(gen_pop,tot_pop): # Probability of Parent 2 being of that genotype
    prob = (gen_pop - 1)/(tot_pop-1)
    return prob

def Pr_Event(): #Pr_parent1 x Pr_parent 2 x Fixed_Pr
    
    pass

Pr_desired_Phenotype = 0 # Sum of Pr_Events will be done with for loops

print(tot_pop)'''

def iprb(k, m, n):
    # Calculate the probability of two randomly selected organisms producing an individual
    # with a dominant phenotype, based on the given numbers of organisms with different genotypes

    # Calculate the numerator of the probability equation
    i = m * m + 4 * n * n + 4 * m * n - 4 * n - m

    # Calculate the denominator of the probability equation
    j = 4 * (k + m + n) * (k + m + n - 1)

    # Calculate the probability of producing an individual with a dominant phenotype
    rst = 1 - float(i) / j

    return rst

print(iprb(17, 29, 20))  # Print the probability of producing an individual with a dominant phenotype

'''

if __name__ == "__main__":
    with open("../data/rosalind_iprb.txt", 'r') as f:
        k, m, n = map(int, f.readline().strip().split(" "))
'''
