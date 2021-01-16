

def cmn2(l,m,n):
    if m == 0:
        return []
    if m > len(l):
        return []
    choose = cmn2(l[1:],m-1,n)
    un_choose = cmn2(l[1:],m,n)
    [[l[0],] + [each for each in choose]]
    return result


if __name__ == '__main__':
    ll = cmn2(['1','2','3','4','5'], 5, 3)
    print(ll)
