# Rule-N

Rule-N is a script that let's you visualise any possible [elementary cellular automaton](https://en.wikipedia.org/wiki/Elementary_cellular_automaton), where N is the Wolfram code

## Usage

The script has 2 arguments, `rule` and `length` (`len` for short)

`rule` is the rule the cellular automaton will follow

`lenth` is the amount of cells the automaton will have, in other words, the length of the list of cells

Running the script without arguments will default to rule 110 with a length of 60 cells

To pass in a rule or length, use the `--flag` or `--length`/`--len` followed by the desired value

## Examples

Arguments: 10 generations, length of 20

`python3 rule-n.py --len 20 --rule [example]` 

Length was hardcoded, argument to be implemented in the future

### Rule 18

```
          #         
         # #        
        #   #       
       # # # #      
      #       #     
     # #     # #    
    #   #   #   #   
   # # # # # # # #  
  #               # 
 # #             # #
```

### Rule 22

```
          #         
         ###        
        #   #       
       ### ###      
      #       #     
     ###     ###    
    #   #   #   #   
   ### ### ### ###  
  #               # 
 ###             ###
```

### Rule 30

```
          #         
         ###        
        ##  #       
       ## ####      
      ##  #   #     
     ## #### ###    
    ##  #    #  #   
   ## ####  ######  
  ##  #   ###     # 
 ## #### ##  #   ###
```

### Rule 60

```
          #         
          ##        
          # #       
          ####      
          #   #     
          ##  ##    
          # # # #   
          ########  
          #       # 
          ##      ##
```

### Rule 110

```
          #         
         ##         
        ###         
       ## #         
      #####         
     ##   #         
    ###  ##         
   ## # ###         
  ####### #         
 ##     ###         
```

## TODO

- [ ] Custom number of generations rather than a forever loop
- [ ] Custom delay
- [ ] Custom seed
