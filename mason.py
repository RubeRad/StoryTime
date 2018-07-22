#Mason J Settergren 7/13/18
#text rpg

import random


life = 100
gold = 100

def path1(life, gold):
    path1_1 = input('north, south, east, or west: \n >')
    if path1_1 == 'north':
        path1_1_1 = input('you see a giant. fight or flight')
        if path1_1_1 == 'fight':
            life -= 10
            print('the giant dies. you lose 10 life. you have ' + str(life) + ' life')
        elif path1_1_1 == 'flight':
            gold -= 10
            print('you flee, but the giant steals 10 gold. you have ' + str(gold) + ' gold')
    elif path1_1 == 'south':
        path1_1_2 = input('you see a treasue chest. take or leave')
        if path1_1_2 == 'take':
            life -= 5
            gold += 20
            print('you open the chest and are bit by a snake inside. you lose 5 life but get 20 gold! you have ' + str(life) + ' life and '+ str(gold) + ' gold')
        elif path1_1_2 == 'leave':
            life -= 5
            gold += 20
            print('don\'t lie to yourself. you open the chest and are bit by a snake inside. you lose 5 life but get 20 gold! you have ' + str(life) + ' life and '+ str(gold) + ' gold')
    elif path1_1 == 'east':
        path1_1_3 = input('you see a bottle. drink or leave')
        if path1_1_3 == 'drink':
            print('you drink the bottle. nothing happens.')
        elif path1_1_3 == 'leave':
            print('you leave the bottle')

    elif path1_1 == 'west':
        path1_1_4 = input('you see a thorny bush. reach in or leave it')
        if path1_1_4 == 'reach in':
            life -= 5
            gold += 5
            print('you reach in. the thorns poke you and you lose 5 life, but you grab 5 gold inside. you have ' + str(life) + ' life and ' + str(gold) + ' gold')

        elif path1_1_4 == 'leave it':
            print('you leave the bush')

    return {life, gold}


def path2(life, gold):
    path2_1 = input('north, south, east, or west')
    if path2_1 == 'north':
        path2_1_1 = input('you see a ship. investigate or leave')
        if path2_1_1 == 'investigate':
            path2_1_1_1 = input('you enter the ship. there are two corridors. right or left')
            if path2_1_1_1 == 'right':
                gold += 20
                print('a pirate ghost attacks you, but he phases through you. you steal the gold behind him. you have ' + str(gold) + ' gold')
            elif path2_1_1_1 == 'left':
                life += 20
                print('a pirate ghost attacks you, but he phases through you. you steal the potion behind him and drink it. you have ' + str(life) + ' life')
        elif path2_1_1 == 'leave':
            print('you leave the ship')
    elif path2_1 == 'south':
        path2_1_2 = input('you see a building. investigate or leave')
        if path2_1_2 == 'investigate':
            path2_1_2_1 = input('you enter the building. there are two corridors. right or left')
            if path2_1_2_1 == 'right':
                gold -= 20
                print('you walk in. a metal arm grabs you and steals 20 gold. you have ' + str(gold) + ' gold')
            elif path2_1_2_1 == 'left':
                life -= 20
                print('you walk left. a gas fills the room. you fall asleep. you wake up groggy. you have ' + str(life) + 'life')
        elif path2_1_2 == 'leave':
            print('you leave the building')
    elif path2_1 == 'east':
        path2_1_3 = input('you see a bathtub. do you bathe in it or leave? \(y/n\)')
        if path2_1_3 == 'y':
            print('you bathe in the bathtub. nothing happens')
        elif path2_1_3 == 'n':
            print('you leave the bathtub')

    elif path2_1 == 'west':
        path2_1_4 = input('you see a hole. you can\'t see the bottom. jump in or leave')
        if path2_1_4 == 'jump in':
            life = 10
            gold += 500
            print('you fall for several minutes. you fall onto a mattress. you barely survive, but you enter a giant room full of gold. you have 10 life and ' + gold + ' gold')
        elif path2_1_4 == 'leave':
            print('you leave the hole.')


path_results1 = [life, gold]
life = path_results1
gold = path_results1[1]

path2(life, gold)
print('the end')