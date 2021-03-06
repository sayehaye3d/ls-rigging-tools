'''
Created on May 20, 2014

@author: Leon
'''
import pymel.core as pm
import pymel.core.nodetypes as nt
'''
# rename all shape nodes by parent
nodes = pm.ls(dag=True)
for n in nodes:
    if isinstance(n, nt.Shape):
        parentName = n.getParent().nodeName()
        newShapeName = parentName+'Shape'
        print 'renaming %s to %s' % (n.nodeName(), (parentName+'Shape'))
        if n.nodeName() != newShapeName:
            n.rename(parentName+'Shape')
            
# rename all effectors by ikHdls
for n in nodes:
    if isinstance(n, nt.IkEffector):
        newName = n.hp.get().nodeName()+'_ee'
        n.rename(newName)
        
# add token to name
for n in nodes:
    tokens = n.nodeName().split('_')
    tokens.insert(1, 'spline')
    newName = '_'.join(tokens)
    n.rename(newName)
    
    
# non-unique names
nodes = pm.ls(dag=True)
nonUniqueNodes = []
for n in nodes:
    if '|' in n.name():
        print n
        nonUniqueNodes.append(n)
pm.select(nonUniqueNodes)

# find child nodes that have same name as parent
# add an alphabet
for n in nodes:
    parentNode = n.getParent()
    if parentNode:
        if n.nodeName() == parentNode.nodeName():
            print n
            '''
            
# rename curve shape based on xfo
def renameCurvesBasedOnXfo(xfo):
    '''
    import rigger.utils.names as names
    xfos = pm.ls(sl=True, type='transform')
    for xfo in xfos:
        names.renameCurvesBasedOnXfo(xfo)
    '''
    shapes = xfo.getChildren(s=True)
    for _i, shape in enumerate(shapes):
        print _i
        print shape
        if str(shape)[-4:] == 'Orig':
            shape.rename(xfo+'Shape%dOrig'%_i)
        elif str(shape)[-4:] == 'Deformed':
            shape.rename(xfo+'Shape%dDeformed'%_i)
        else:
            shape.rename(xfo+'Shape%d'%_i)