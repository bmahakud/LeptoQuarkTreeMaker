import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/02D83B4D-8116-E511-A33F-001E673983A4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/244A01DC-1116-E511-99C3-AC853DA06B7A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/3C318B5B-8116-E511-898E-002590AC4C6E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/52273956-8116-E511-920C-0025905B85E8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/6CAAA66B-FD15-E511-AE44-002590A2CCE6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/6E699B36-8116-E511-8D99-C4346BBF3E78.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/76FB7C7D-CE15-E511-8046-1CC1DE046F18.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/7CE44DDD-D115-E511-A5B1-842B2B185470.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/800532A0-BA15-E511-8C8B-0025905A60EE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/8203DD9A-BA15-E511-A1D4-0025905A608C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/86859DF7-D015-E511-B48E-842B2B185470.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/A20C7756-8116-E511-8C2C-0025905A607A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/A288A0AE-C015-E511-BC3C-0025905B85A2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/A43D0F0B-C115-E511-B08D-0025905B859E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/ACC2B458-8116-E511-B645-00266CFFA604.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/C6B548D3-CA15-E511-8ACB-001E67396F9A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/CC25AB97-BA15-E511-9D62-0025905A608C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/DA317793-BA15-E511-9C49-0025905B859E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/E4C81B74-FD15-E511-B219-0025901D4AF0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/E65D805E-C715-E511-83EB-0025905A607A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/E81AC896-BA15-E511-99D7-003048FFD740.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/E8D5E0E4-7916-E511-A398-00266CF258D8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/FC419B92-BA15-E511-8EC7-0025905A60CA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/0067FB41-4016-E511-AB7B-001E67396D42.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/0CF57FF3-3D16-E511-9762-001E67396897.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/16AC9340-AD16-E511-B68B-00266CFFA678.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/1C23C74C-3716-E511-AE9E-6CC2173BC850.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/1CDD4C53-3716-E511-AFB7-AC853D9DACE3.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/1EE39841-4016-E511-BBCB-001E673971CA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/32A82CEB-3D16-E511-9180-002590A80E08.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/34E82747-4016-E511-AFB7-002590200948.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/36D7314F-B115-E511-8420-00A0D1EE95FC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/384CEA23-0216-E511-B833-002618943809.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/38F1C3F5-B115-E511-BB5F-008CFA002ED8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/3CDC7551-3716-E511-93A6-00266CFFCB14.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/3E24CCF8-AD16-E511-8392-E41D2D08DEB0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/40DD237E-3E16-E511-9A84-002590A831DC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/46665B26-0216-E511-BC87-0025905B85EE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/4696BB9E-C715-E511-841F-001E68864FF4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/4A5F4E56-3716-E511-8CE7-00266CFFC9EC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/4C811514-B215-E511-A968-00A0D1EE8C64.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/5084D35A-3716-E511-968B-782BCB407CFD.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/50E19CC7-3F16-E511-A9E7-001E67397E1D.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/52C1FF40-4016-E511-87D0-002590A831B6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/52CC51A5-C015-E511-BE81-00266CF9B318.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/52E5B1E5-C515-E511-8E7E-AC853D9F5120.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/52FE1F51-3716-E511-9777-00266CFFBE88.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/546D81F4-0216-E511-83DE-00261894393A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/58A747C7-3F16-E511-91B6-002590FC5ACC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/5C0C5CBE-0216-E511-A793-002618943971.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/5E33D4F9-BC15-E511-84F2-3417EBE6444A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/66717595-8D17-E511-8A5F-E41D2D08DE50.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/686C7752-3716-E511-8CC0-6CC2173BBEC0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/6A8027D4-AD16-E511-A42D-047D7BD6DEFA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/6A9A0925-B715-E511-8A76-00266CFADE34.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/6CD2977F-0216-E511-BB14-0025905A6138.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/6EE41BCD-1117-E511-A11A-6CC2173BC990.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/72814E12-4016-E511-B856-001E673982E6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/74AAFA96-0216-E511-8B32-002590596486.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/7644572E-4016-E511-B0AE-001E67396905.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/768AD59A-C415-E511-BD0D-00266CF27130.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/76A4E3D8-AD16-E511-9A0A-0025907FD424.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/76F347F5-B115-E511-882C-00266CFAE30C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/78C296E9-611A-E511-82C1-842B2B1858FB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/78F69C56-3716-E511-A128-000F53273500.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/7AF33753-3716-E511-9A9E-B083FED76DBD.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/7E4D005D-0216-E511-A08B-002618943949.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/7EB5CFB3-881A-E511-8D21-00261894393E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/806D35F7-B115-E511-9FE4-00266CF2507C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/86D98FA8-C015-E511-BF46-00266CF9BDFC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/86E9AA27-B715-E511-8D1A-3417EBE50720.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/8AF96CA7-C015-E511-BAE3-00266CF25490.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/8C046511-891A-E511-B80B-842B2B2AEE84.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/92764352-3716-E511-92DC-00266CFFCB14.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/92EC7343-4016-E511-9D7A-002590FC5AD0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/9431ACBE-8F17-E511-A3C6-002590DB91CA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/94DA22FA-3F16-E511-955D-001E67398633.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/96D4F1A9-C015-E511-9405-008CFA0104E0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/9C1F7D9C-A917-E511-B25B-00A0D1EE89E0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/9C6F90DB-3F16-E511-AB2B-001E6739839A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/9E9B42B1-6B16-E511-9FF9-002590A81DAC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/A6A5AD4F-3716-E511-AAED-C4346BBC9BB0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/A8BFA74D-3716-E511-B317-6CC2173BB820.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/B6C7C34B-0216-E511-81CF-0025905A6088.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/B6D00AF2-B115-E511-91E4-00A0D1EEE5CC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/BAA66A42-4016-E511-B772-002590A8880A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/BE06A940-4016-E511-89A1-002590A887F0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/BE682E22-4016-E511-96BA-001E673973C8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/C01FF323-0216-E511-B977-002618943809.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/C2711EEA-0216-E511-8EA1-0025905A60B0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/C274E851-3716-E511-B3B9-AC853DA06A1A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/CA91EC1C-B715-E511-A06E-00A0D1EE965C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/CC1565F6-B115-E511-BDE3-00266CF2580C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/CC25287D-0216-E511-819D-0025905A4964.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/CE822B61-0216-E511-8AF7-0025905A6138.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/D41AC274-BF15-E511-BBE4-3417EBE6444A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/D42ED875-0216-E511-8DD7-002618943971.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/D684FDCE-AD16-E511-862D-0025907DC9D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/D6ED6185-0216-E511-A89A-0025905A6126.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/D820AD14-B215-E511-9DBC-00A0D1EE965C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E01DED53-3716-E511-9DA2-00266CFE79A4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E02BCF5E-3716-E511-AB54-0026B95CE867.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E2CA4A58-7017-E511-927B-002481E14FEE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E42290F1-611A-E511-A525-000F53273650.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E4CA6651-3716-E511-839D-AC162DA87230.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E6601AEE-AD16-E511-B3DC-0025904B1446.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E6671C12-BE15-E511-ADAB-00266CF2679C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E6D1F5F2-CA16-E511-8B1F-00266CF9B4C0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E88FFBBE-0216-E511-8506-0025905964A2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/EC83C3DD-881A-E511-8441-0025905AA9CC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/ECB50DE2-0216-E511-A375-002618943857.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/F48A155F-3716-E511-BE74-0026B95B8B31.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/FA3551E4-611A-E511-A718-AC853DA06B56.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/FC7331EC-3D16-E511-9461-001E673967C5.root' ] );


secFiles.extend( [
               ] )

