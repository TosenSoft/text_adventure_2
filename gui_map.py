class Map:
    def __init__(self, canv, charpos):
        self.c = canv
        self.charpos = charpos
        self.max_width = 220
        self.max_height = 180
        self.start_p = 2
        self.dim1 = 100
        self.dim2 = 70
        self.dim3 = 100
        self.dim4 = 70
        self.dim5 = 100
        self.dim6 = 70
        self.dim7 = 100
        self.dim8 = 70
        self.dim9 = 100
        self.dim10 = 50
        self.dim11 = 40
        self.dim12 = 30
        self.dim13 = 110
        self.dim14 = 140
        self.dim15 = 60
        self.dim16 = 100
        self.x1 = (self.max_width-self.dim1)/2
        self.y1 = (self.max_height-self.dim2)/2
        self.x2 = (self.max_width-self.dim3)/2
        self.y2 = (self.max_height-self.dim4)/2
        self.x3 = (self.max_width-self.dim5)/2
        self.y3 = (self.max_height-self.dim6)/2
        self.x4 = (self.max_width-self.dim7)/2
        self.y4 = (self.max_height-self.dim8)/2
        self.x5 = (self.max_width-self.dim9)/2
        self.y5 = (self.max_height-self.dim10)/2
        self.x6 = (self.max_width-self.dim11)/2
        self.y6 = (self.max_height-self.dim12)/2
        self.x7 = (self.max_width-self.dim13)/2
        self.y7 = (self.max_height-self.dim14)/2
        self.x8 = (self.max_width-self.dim15)/2
        self.y8 = (self.max_height-self.dim16)/2
        self.r1 = [self.x1, self.y1, self.x1+40, self.y1, self.x1+40, self.y1+20, self.x1, self.y1+20]
        self.r2 = [self.x1, self.y1+20, self.x1+20, self.y1+20, self.x1+20, self.y1+50, self.x1, self.y1+50]
        self.r3 = [self.x1, self.y1+50, self.x1+40, self.y1+50, self.x1+40, self.y1+70, self.x1, self.y1+70]
        self.r4 = [self.x1+40, self.y1, self.x1+60, self.y1, self.x1+60, self.y1+20, self.x1+40, self.y1+20]
        self.r5 = [self.x1+20, self.y1+20, self.x1+80, self.y1+20, self.x1+80, self.y1+50, self.x1+20, self.y1+50]
        self.r6 = [self.x1+60, self.y1, self.x1+100, self.y1, self.x1+100, self.y1+20, self.x1+60, self.y1+20]
        self.r7 = [self.x1+80, self.y1+20, self.x1+100, self.y1+20, self.x1+100, self.y1+70, self.x1+60, self.y1+70,
                   self.x1+60, self.y1+50, self.x1+80, self.y1+50, self.x1+80, self.y1+20]
        self.r8 = [self.x2, self.y2, self.x2+10, self.y2, self.x2+10, self.y2+20, self.x2+40, self.y2+20, self.x2+40,
                   self.y2+40, self.x2, self.y2+40, self.x2, self.y2]
        self.r9 = [self.x2, self.y2+40, self.x2+20, self.y2+40, self.x2+20, self.y2+70, self.x2, self.y2+70]
        self.r10 = [self.x2+10, self.y2, self.x2+60, self.y2, self.x2+60, self.y2+20, self.x2+10, self.y2+20]
        self.r11 = [self.x2+20, self.y2+40, self.x2+40, self.y2+40, self.x2+40, self.y2+70, self.x2+20, self.y2+70]
        self.r12 = [self.x2+40, self.y2+20, self.x2+60, self.y2+20, self.x2+60, self.y2+40, self.x2+40, self.y2+40]
        self.r13 = [self.x2+40, self.y2+40, self.x2+60, self.y2+40, self.x2+60, self.y2+70, self.x2+40, self.y2+70]
        self.r14 = [self.x2+60, self.y2, self.x2+80, self.y2, self.x2+80, self.y2+40, self.x2+60, self.y2+40]
        self.r15 = [self.x2+60, self.y2+40, self.x2+80, self.y2+40, self.x2+80, self.y2+70, self.x2+60, self.y2+70]
        self.r16 = [self.x2+80, self.y2, self.x2+100, self.y2, self.x2+100, self.y2+20, self.x2+80, self.y2+20]
        self.r17 = [self.x2+80, self.y2+20, self.x2+100, self.y2+20, self.x2+100, self.y2+70, self.x2+80, self.y2+70]
        self.r18 = [self.x3, self.y3, self.x3+50, self.y3, self.x3+50, self.y3+20, self.x3+20, self.y3+20, self.x3+20,
                    self.y3+30, self.x3, self.y3+30, self.x3, self.y3]
        self.r19 = [self.x3, self.y3+30, self.x3+20, self.y3+30, self.x3+20, self.y3+70, self.x3, self.y3+70]
        self.r20 = [self.x3+20, self.y3+20, self.x3+50, self.y3+20, self.x3+50, self.y3+40, self.x3+20, self.y3+40]
        self.r21 = [self.x3+20, self.y3+40, self.x3+50, self.y3+40, self.x3+50, self.y3+70, self.x3+20, self.y3+70]
        self.r22 = [self.x3+50, self.y3, self.x3+80, self.y3, self.x3+80, self.y3+20, self.x3+50, self.y3+20]
        self.r23 = [self.x3+50, self.y3+20, self.x3+80, self.y3+20, self.x3+80, self.y3+70, self.x3+50, self.y3+70]
        self.r24 = [self.x3+80, self.y3, self.x3+100, self.y3, self.x3+100, self.y3+30, self.x3+80, self.y3+30]
        self.r25 = [self.x3+80, self.y3+30, self.x3+100, self.y3+30, self.x3+100, self.y3+70, self.x3+80, self.y3+70]
        self.r26 = [self.x4, self.y4, self.x4+30, self.y4, self.x4+30, self.y4+20, self.x4, self.y4+20]
        self.r27 = [self.x4, self.y4+20, self.x4+20, self.y4+20, self.x4+20, self.y4+40, self.x4, self.y4+40]
        self.r28 = [self.x4, self.y4+40, self.x4+30, self.y4+40, self.x4+30, self.y4+70, self.x4, self.y4+70]
        self.r29 = [self.x4+20, self.y4+20, self.x4+50, self.y4+20, self.x4+50, self.y4+40, self.x4+20, self.y4+40]
        self.r30 = [self.x4+50, self.y4+20, self.x4+70, self.y4+20, self.x4+70, self.y4+50, self.x4+30, self.y4+50,
                    self.x4+30, self.y4+40, self.x4+50, self.y4+40]
        self.r31 = [self.x4+70, self.y4, self.x4+100, self.y4, self.x4+100, self.y4+20, self.x4+70, self.y4+20]
        self.r32 = [self.x4+70, self.y4+20, self.x4+100, self.y4+20, self.x4+100, self.y4+50, self.x4+70, self.y4+50]
        self.r33 = [self.x4+70, self.y4+50, self.x4+100, self.y4+50, self.x4+100, self.y4+70, self.x4+70, self.y4+70]
        self.r34 = [self.x5, self.y5, self.x5+30, self.y5, self.x5+30, self.y5+20, self.x5, self.y5+20]
        self.r35 = [self.x5, self.y5+20, self.x5+30, self.y5+20, self.x5+30, self.y5+50, self.x3, self.y5+50]
        self.r36 = [self.x5+30, self.y5, self.x5+70, self.y5, self.x5+70, self.y5+10, self.x5+30, self.y5+10]
        self.r37 = [self.x5+30, self.y5+10, self.x5+70, self.y5+10, self.x5+70, self.y5+40, self.x5+30, self.y5+40]
        self.r38 = [self.x5+30, self.y5+40, self.x5+70, self.y5+40, self.x5+70, self.y5+50, self.x5+30, self.y5+50]
        self.r39 = [self.x5+70, self.y5, self.x5+100, self.y5, self.x5+100, self.y5+50, self.x5+70, self.y5+50]
        self.r40 = [self.x6, self.y6, self.x6+40, self.y6, self.x6+40, self.y6+30, self.x6, self.y6+30]
        self.r41 = [self.x7+40, self.y7, self.x7+60, self.y7, self.x7+60, self.y7+20, self.x7+40, self.y7+20]
        self.r42 = [self.x7, self.y7+20, self.x7+40, self.y7+20, self.x7+40, self.y7+40, self.x7, self.y7+40]
        self.r43 = [self.x7, self.y7+110, self.x7+50, self.y7+110, self.x7+50, self.y7+130, self.x7, self.y7+130]
        self.r44 = [self.x7+40, self.y7+20, self.x7+70, self.y7+20, self.x7+70, self.y7+60, self.x7+60, self.y7+60,
                    self.x7+60, self.y7+100, self.x7+50, self.y7+100, self.x7+50, self.y7+60, self.x7+40, self.y7+60,
                    self.x7+40, self.y7+20]
        self.r45 = [self.x7+50, self.y7+100, self.x7+60, self.y7+100, self.x7+60, self.y7+140, self.x7+50, self.y7+140]
        self.r46 = [self.x7+70, self.y7+20, self.x7+100, self.y7+20, self.x7+100, self.y7+40, self.x7+70, self.y7+40]
        self.r47 = [self.x7+60, self.y7+110, self.x7+110, self.y7+110, self.x7+110, self.y7+130, self.x7+60, self.y7+130]
        self.r48 = [self.x8+30, self.y8, self.x8+40, self.y8, self.x8+40, self.y8+20, self.x8+30, self.y8+20]
        self.r49 = [self.x8, self.y8+50, self.x8+20, self.y8+50, self.x8+20, self.y8+60, self.x8, self.y8+60]
        self.r50 = [self.x8+30, self.y8+80, self.x8+40, self.y8+80, self.x8+40, self.y8+100, self.x8+30, self.y8+100]
        self.r51 = [self.x8+20, self.y8+20, self.x8+60, self.y8+20, self.x8+60, self.y8+80, self.x8+20, self.y8+80]
        self.p0d1 = [self.x1+7, self.y1+20, self.x1+13, self.y1+20, self.x1+13, self.y1+50, self.x1+7, self.y1+50]
        self.p0d2 = [self.x1+40, self.y1+7, self.x1+60, self.y1+7, self.x1+60, self.y1+13, self.x1+40, self.y1+13]
        self.p0d3 = [self.x1+47, self.y1+20, self.x1+53, self.y1+20, self.x1+53, self.y1+21, self.x1+47, self.y1+21]
        self.p0d4 = [self.x1+87, self.y1+20, self.x1+93, self.y1+20, self.x1+93, self.y1+21, self.x1+87, self.y1+21]
        self.p1d1 = [self.x2+20, self.y2+57, self.x2+80, self.y2+57, self.x2+80, self.y2+63, self.x2+20, self.y2+63]
        self.p1d2 = [self.x2+47, self.y2+20, self.x2+53, self.y2+20, self.x2+53, self.y2+40, self.x2+47, self.y2+40]
        self.p1d3 = [self.x2+7, self.y2+40, self.x2+13, self.y2+40, self.x2+13, self.y2+41, self.x2+7, self.y2+21]
        self.p1d4 = [self.x2+80, self.y2+7, self.x2+81, self.y2+7, self.x2+81, self.y2+13, self.x2+80, self.y2+13]
        self.p2d1 = [self.x3+7, self.y3+30, self.x3+13, self.y3+30, self.x3+13, self.y3+31, self.x3+7, self.y3+31]
        self.p2d2 = [self.x3+20, self.y3+57, self.x3+50, self.y3+57, self.x3+50, self.y3+63, self.x3+20, self.y3+63]
        self.p2d3 = [self.x3+37, self.y3+40, self.x3+43, self.y3+40, self.x3+43, self.y3+41, self.x3+37, self.y3+41]
        self.p2d4 = [self.x3+67, self.y3+20, self.x3+73, self.y3+20, self.x3+73, self.y3+21, self.x3+67, self.y3+21]
        self.p2d5 = [self.x3+80, self.y3+7, self.x3+81, self.y3+7, self.x3+81, self.y3+13, self.x3+80, self.y3+13]
        self.p2d6 = [self.x3+87, self.y3+20, self.x3+93, self.y3+20, self.x3+93, self.y3+21, self.x3+87, self.y3+21]
        self.p3d1 = [self.x4+7, self.y4+20, self.x4+13, self.y4+20, self.x4+13, self.y4+41, self.x4+7, self.y4+41]
        self.p3d2 = [self.x4+20, self.y4+27, self.x4+50, self.y4+27, self.x4+50, self.y4+33, self.x4+20, self.y4+33]
        self.p3d3 = [self.x4+70, self.y4+32, self.x4+71, self.y4+32, self.x4+71, self.y4+38, self.x4+70, self.y4+38]
        self.p3d4 = [self.x4+82, self.y4+20, self.x4+88, self.y4+20, self.x4+88, self.y4+50, self.x4+82, self.y4+50]
        self.p4d1 = [self.x5+17, self.y5+20, self.x5+23, self.y5+20, self.x5+23, self.y5+21, self.x5+17, self.y5+21]
        self.p4d2 = [self.x5+30, self.y5+27, self.x5+31, self.y5+27, self.x5+31, self.y5+33, self.x5+27, self.y5+33]
        self.p4d3 = [self.x5+47, self.y5+10, self.x5+53, self.y5+10, self.x5+53, self.y5+40, self.x5+47, self.y5+40]
        self.p4d4 = [self.x5+70, self.y5+3, self.x5+71, self.y5+3, self.x5+71, self.y5+7, self.x5+70, self.y5+7]
        self.p6d1 = [self.x7+47, self.y7+20, self.x7+53, self.y7+20, self.x7+53, self.y7+21, self.x7+47, self.y7+21]
        self.p6d2 = [self.x7+40, self.y7+27, self.x7+71, self.y7+27, self.x7+71, self.y7+33, self.x7+40, self.y7+33]
        self.p6d3 = [self.x7+53, self.y7+100, self.x7+57, self.y7+100, self.x7+57, self.y7+101, self.x7+53, self.y7+101]
        self.p6d4 = [self.x7+50, self.y7+117, self.x7+60, self.y7+117, self.x7+60, self.y7+123, self.x7+50, self.y7+123]
        self.d0 = [self.p0d1, self.p0d2, self.p0d3, self.p0d4]
        self.d1 = [self.p1d1, self.p1d2, self.p1d3, self.p1d4]
        self.d2 = [self.p2d1, self.p2d2, self.p2d3, self.p2d4, self.p2d5, self.p2d6]
        self.d3 = [self.p3d1, self.p3d2, self.p3d3, self.p3d4]
        self.d4 = [self.p4d1, self.p4d2, self.p4d3, self.p4d4]
        self.d5 = []
        self.d6 = [self.p6d1, self.p6d2, self.p6d3, self.p6d4]
        self.d7 = []
        self.p0 = [self.r48, self.r49, self.r50, self.r51]
        self.p1 = [self.r41, self.r42, self.r43, self.r44, self.r45, self.r46, self.r47]
        self.p2 = [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7]
        self.p3 = [self.r8, self.r9, self.r10, self.r11, self.r12, self.r13, self.r14, self.r15, self.r16, self.r17]
        self.p4 = [self.r18, self.r19, self.r20, self.r21, self.r22, self.r23, self.r24, self.r25]
        self.p5 = [self.r26, self.r27, self.r28, self.r29, self.r30, self.r31, self.r32, self.r33]
        self.p6 = [self.r34, self.r35, self.r36, self.r37, self.r38, self.r39]
        self.p7 = [self.r40]
        self.visited = [self.r5]
        self.passages = [self.r4, self.r10, self.r16, self.r24, self.r20, self.r29, self.r26, self.r34, self.r41,
                         self.r43, self.r51, self.r37]
        self.planes = ['Piano Bonus', 'Piano Sotterraneo', 'Piano terra', 'I piano', 'II piano', 'III piano',
                       'IV piano, base della torre', 'Cima della Torre']
        self.create_plane(self.c, self.getplane(self.charpos))
        self.idd = self.c.create_text(110, 160, fill='#FA8072', text=self.planes[self.start_p], font=('Tempus Sans ITC', 8, 'bold'))
        self.create_doors(self.c, self.getdoors(self.charpos))
        self.mylocation(self.c, self.getroomid(self.charpos))

    def create_plane(self, cv, val):
            for i in range(len(val)):
                if val[i] not in self.visited:
                    pass
                    # cv.create_polygon(val[i], outline="green", fill="red")
                else:
                    if val[i] in self.passages:
                        cv.create_polygon(val[i], outline="yellow", fill="black")
                    else:
                        cv.create_polygon(val[i], outline="green", fill="black")

    def create_doors(self, cv, val):
        for i in range(len(val)):
                cv.create_polygon(val[i], outline="black", fill="black")

    def getroomid(self, pos):
        if pos <= 7:
            t = pos-1
            return self.p2[t]
        elif (pos > 7) and (pos <= 17):
            t = pos-8
            return self.p3[t]
        elif (pos > 17) and (pos <= 25):
            t = pos-18
            return self.p4[t]
        elif (pos > 25) and (pos <= 33):
            t = pos-26
            return self.p5[t]
        elif (pos > 33) and (pos <= 39):
            t = pos-34
            return self.p6[t]
        elif pos == 40:
            return self.p7[0]
        elif (pos > 40) and (pos <= 47):
            t = pos-41
            return self.p1[t]
        elif (pos > 47) and (pos <= 51):
            t = pos-48
            return self.p0[t]

    def getplane(self, pos):
        if pos <= 7:
            return self.p2
        elif (pos > 7) and (pos <= 17):
            return self.p3
        elif (pos > 17) and (pos <= 25):
            return self.p4
        elif (pos > 25) and (pos <= 33):
            return self.p5
        elif (pos > 33) and (pos <= 39):
            return self.p6
        elif pos == 40:
            return self.p7
        elif (pos > 40) and (pos <= 47):
            return self.p1
        elif (pos > 47) and (pos <= 51):
            return self.p0

    def getdoors(self, pos):
        if pos <= 7:
            return self.d0
        elif (pos > 7) and (pos <= 17):
            return self.d1
        elif (pos > 17) and (pos <= 25):
            return self.d2
        elif (pos > 25) and (pos <= 33):
            return self.d3
        elif (pos > 33) and (pos <= 39):
            return self.d4
        elif pos == 40:
            return self.d5
        elif (pos > 40) and (pos <= 47):
            return self.d6
        elif (pos > 47) and (pos <= 51):
            return self.d7

    def mylocation(self, cv, room):
        cv.create_polygon(room, outline="green", fill="blue")




