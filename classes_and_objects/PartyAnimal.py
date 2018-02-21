class PartyAnimal:
    x=0
    def party(self):
        self.x=self.x+1
        print("So far,",self.x)


test=PartyAnimal()
test.party()
test.party()
print(test.x)
an=PartyAnimal()
an.party()
df=PartyAnimal()
PartyAnimal.party(df)