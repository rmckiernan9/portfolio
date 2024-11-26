import csv


def load_regions(filename): #Re-structured to sort by population
    states_dict = dict()
    with open(filename, 'r') as f:
        for line in csv.reader(f):
            states_dict[line[1]] = int(line[3])
        
        states_sort = sorted(states_dict.items(),key=lambda x:x[1],\
                             reverse=True)
        states_sortD = dict(states_sort)
    return states_sortD 


def load_borders(filename):
    borders_list = list()

    with open(filename, 'r') as f:
        for line in csv.reader(f, 1):
            states = line[1].split('-')
            if len(states) == 2:
                borders_list.append((states[0], states[1]))

    return borders_list


# This function returns the state and population of the "most populous
# neighbor" bordering the candidate nation.
def most_populous_neighbor(states, borders, nation):
    neighbor = ''
    pop = 0

    for s in nation:
        for border in borders:
            if border[0] == s and border[1] in states:
                candidate = border[1]
                candidate_pop = states[border[1]]

                if candidate not in nation and candidate_pop > pop:
                    neighbor = candidate
                    pop = candidate_pop
                    
                    #print(neighbor)
                    #print(pop)

            if border[1] == s and border[0] in states:
                candidate = border[0]
                candidate_pop = states[border[0]]

                if candidate not in nation and candidate_pop > pop:
                    neighbor = candidate
                    pop = candidate_pop

    return neighbor, pop

def nation_combos(n,nation,borders,states):
        new_nation_combos = nation #Starts as a list with one tuple, one state
        pop_combos = []
        size = 1
        end_states = []

     #while n > size:
            
        #Step 1: create end states list
        if len(new_nation_combos) == 1:
            end_states.append(new_nation_combos)
        else:
            for a in new_nation_combos:
                end_states.append(a[-1])
        #print(end_states)
              
        #Step 2: Check neighbors,
        for d in new_nation_combos:
            for c in end_states:    
                for b in borders:
                    if b[0] == c:
                        cand = tuple(b[1])
                        if cand not in d:
                            new_combo = d + cand
                            new_nation_combos.append(new_combo)
                    if b[1] == c:
                        cand = tuple(b[0])
                        if cand not in d:
                            new_combo = d + cand
                            new_nation_combos.append(new_combo)
            
        print(new_nation_combos)
                    
        
  #      for d in new_nation_combos:
   #           for e in new_nation_combos[d]:
      #             pop_combos.append(states[borders[e]])
                    
      
        #return (max(new_nation_combos),max(pop_combos)
            #Get Neighbors of particular end state
            
            
        #grab end states, check for neighbors not in nation and if candidate state is most populous
        #then yeet it on





def new_nation_n_states(n, reg_filename, border_filename):
    new_nation = []
    max_pop = 0

    states = load_regions(reg_filename)
    borders = load_borders(border_filename)

    # Our naive implementation arbitrarily starts with the 'first' state
    # returned by load_states. One easy improvement would be to replace this
    # with the most populous state, but you can do far better than this!
    starting_state = list(states.keys())[0]
    new_nation = (starting_state,)
    max_pop = states[starting_state]

    # This is a "greedy" algorithm - we simply find the most populous
    # state bordering our candidate nation and append it to the list.
    while len(new_nation) < n:
        next_st, pop = most_populous_neighbor(states, borders, new_nation)
    #   new_nation, nax_pop = nation_combos(n,new_nation,borders,states)
        new_nation += (next_st,)
        max_pop += pop
        
        print(new_nation)

    return new_nation, max_pop
