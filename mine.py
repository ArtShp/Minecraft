from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

air = 0
x = 0
y = 80
z = 0
bT = 41
mc.player.setPos(0, 80, 15)
mc.setBlocks(x-1, y-1, z-1, x+8+1, y+5+1, z+8+1, air)

for i in range(0, 5):
    for j in range(0, 8):
        time.sleep(0.1)
        mc.setBlock(0+j, 80+i, 0, bT)
    for j in range(0, 8):
        time.sleep(0.1)
        mc.setBlock(0+8, 80+i, 0+j+1, bT)
    for j in range(8, 0, -1):
        time.sleep(0.1)
        mc.setBlock(0+j-1, 80+i, 0+8+1, bT)
    for j in range(8, 0, -1):
        time.sleep(0.1)
        mc.setBlock(0-1, 80+i, 0+j, bT)