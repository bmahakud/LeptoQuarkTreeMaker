import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/16676B26-FA0F-E511-B59C-00266CF2506C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/189E9F88-F30F-E511-A3CB-00266CF9B9F0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/2E9698BD-6011-E511-BB4C-002354EF3BE4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/449722D6-2A10-E511-84CB-002590AC504A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/46CC7FCD-B210-E511-B6BD-001E67398DE5.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/58690DD8-2A10-E511-9E8B-002590AC4CA6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/6A1CBBED-F20F-E511-A031-7845C4F915E2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/6E65496A-4D12-E511-8181-000F532734A4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/706ACEE0-4F12-E511-9269-002590AC4D32.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/7A6ECF99-F30F-E511-B79E-00A0D1EE9274.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/80FE9696-F30F-E511-B40A-3417EBE34C81.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/8292B04B-2A10-E511-9F82-002590AC4CC4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/9006774A-2811-E511-8F6E-00266CFAE788.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/A660D639-1A10-E511-84E9-782BCB40844A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/AE87729A-F30F-E511-87A1-3417EBE65E39.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/B4A65457-2A10-E511-A5AF-002590AC4C74.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/CA73B128-F60F-E511-B6F5-848F69FD501E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/CCD27BCD-2A10-E511-8C8A-002590DB9182.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/D6A0B16F-8910-E511-BE54-0025905B860E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/D86C87EA-F20F-E511-A056-7845C4FC37AF.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/DA621CAF-1410-E511-8593-848F69FD29BB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/E08E13CE-5C11-E511-A68F-B083FED76520.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/ECD489F5-F50F-E511-90FA-F04DA275987A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/EEFAE5B0-6A10-E511-9F30-782BCB407D84.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/00000/F250F4C0-2E10-E511-BE13-002590AC504A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/0296B27A-2A10-E511-A938-008CFA001444.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/02CE731F-3210-E511-837E-B083FED76D99.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/0663BE0F-2B11-E511-A8EE-00266CF27130.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/06B5F327-9B10-E511-B16B-0025905A609A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/0C038B28-9B10-E511-AC0A-003048FFD7BE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/0E90F330-9B10-E511-BB2C-0025905964CC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/14649028-9B10-E511-AED9-0025905B85AA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/1E3A106B-9311-E511-8D90-001E673976D9.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/24173B29-9B10-E511-B59F-0025905A60E4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/2A37E32B-2A10-E511-882F-7845C4FC3C56.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/3CBC1929-9B10-E511-A286-0025905B85D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/3CE32E24-9B10-E511-802C-002618B27F8A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/40053A2F-9B10-E511-BCD6-0025905A610A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/4055E676-2A10-E511-BDCF-3417EBE34BB8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/40C73332-9B10-E511-8CF4-0025905A606A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/56BCCD2F-2B10-E511-8889-008CFA002028.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/5A9B1F74-2A10-E511-97D1-00266CFAE790.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/5E14D735-2A10-E511-814C-00266CFFA754.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/5E213232-2A10-E511-A49C-047D7B881D76.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/6214D038-2A10-E511-BE66-00266CFFA184.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/628E3029-9B10-E511-B0A9-0025905B85AA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/629FF228-9B10-E511-B3FF-0025905B8606.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/6645422A-9B10-E511-9CDA-0025905A610C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/6AEE6126-9B10-E511-8F15-002618943836.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/6C44B72D-9B10-E511-BBF7-00261894388B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/6E3E582C-9B10-E511-90C7-003048FFD754.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/702EFEF7-3710-E511-A04A-3417EBE64C0C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/747CB463-3210-E511-A617-782BCB407D84.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/74B56A66-2C10-E511-A468-008CFA007CE0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/7826CD29-9B10-E511-A9BB-0025905B8590.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/786F6926-9B10-E511-92A5-002618943836.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/7A558602-3810-E511-99CE-7845C4FC3CA1.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/7AB1934E-3210-E511-82D2-B083FED76DB1.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/7E6C6C32-2A10-E511-AAC0-003048F02CB8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/80727E24-9B10-E511-9091-00248C55CC62.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/8ACE9A94-2B10-E511-BE02-00266CF25998.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/8C4ECC82-2A10-E511-9E65-7845C4FC370A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/8CC66028-9B10-E511-B155-003048FFD752.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/969CE2EF-2B10-E511-AFD6-00A0D1EE8A0C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/98A3D53B-2A10-E511-B1BF-047D7BD6DEFA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/98DEF1F8-3810-E511-9A77-00A0D1EEF204.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/9C3341A9-2B10-E511-84A2-00266CFAC6D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/A0C3572A-9B10-E511-95F4-0025905A48D8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/A6918634-2A10-E511-BC66-0025901D493A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/A6A11FA8-2B10-E511-A6AD-00266CF9AE10.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/A8290598-2B10-E511-B451-00266CFAEC8C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/AA4A3974-2A10-E511-948F-008CFA0004B0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/AE81B429-9B10-E511-B33A-0025905A60B8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/B0A74938-2A10-E511-A3ED-003048F0EBBE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/B0B0AF25-9B10-E511-9CCF-002618943918.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/B63BAFA0-2B10-E511-B9AB-008CFA0025A4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/B6BBDD27-9B10-E511-B235-003048FFD7D4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/B6DD0859-2C10-E511-AD04-3417EBE645A9.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/B8BC64AF-5B11-E511-9DC2-0025907FD2DA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/B8D9B331-9B10-E511-AEAC-0025905A6094.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/B8FC4E8A-2A10-E511-9D7A-00A0D1EE29B8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/BC4E8CCE-2A10-E511-8725-00266CF9B034.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/BC8FEAEA-9B10-E511-8797-0025905A610C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/C00E516F-9C10-E511-8D9D-00261894388B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/C0523E67-8111-E511-8F17-B083FED76DBD.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/C06E9658-2C10-E511-9562-3417EBE2EC98.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/C4E90D22-7011-E511-97E8-0025905A60A6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/C8016638-3210-E511-942C-782BCB6E1220.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/C810B926-9B10-E511-BF12-00261894382D.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/CABE4934-2A10-E511-83EF-002481E0EA70.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/CEC7B8D4-2B10-E511-BDCE-008CFA002434.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/D4770D35-2A10-E511-8FFF-002590DB9262.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/E24B3924-8C10-E511-82DE-0026B95CD814.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/ECE5169A-2B10-E511-BA53-00266CF9AD34.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/EEF8CC2C-9B10-E511-97FD-0025905A7786.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/F000EEFF-3310-E511-9BA6-B083FED7685B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/10000/F2402B76-2A10-E511-AB8B-3417EBE34CAB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/12C1516F-ED14-E511-BFC9-842B2B2AEE96.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/20FE3408-1C15-E511-BAB4-1CC1DE046F18.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/34999EF9-1B15-E511-B2AC-000F530E4644.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/48745404-1C15-E511-A291-0025905A60EE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/4A4CC651-0015-E511-BD4C-782BCB285E3F.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/54324B77-F714-E511-97C4-0025905A608A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/74B426F8-1B15-E511-BF04-000F530E4644.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/8039A709-1C15-E511-AA5B-0025904B130A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/8ED3F483-ED14-E511-BB0F-AC853DA06B7A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/AE712F86-ED14-E511-AB73-842B2B2B0CFE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/BCFCD0B4-ED14-E511-8A22-842B2B29C638.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/C2C2BF07-1C15-E511-893C-842B2B298D4E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/E6ACED77-F714-E511-AF29-0025905A60FE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/F2C5B861-FF14-E511-8DA1-78E7D1E49636.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/F42F1251-FF14-E511-88C1-1CC1DE1D1F80.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/F8AC1AD8-EE14-E511-96FF-AC853D9DAC23.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/50000/FA372D81-0015-E511-A2BD-000F530E4644.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/061AEBE1-2010-E511-825B-0025905A60F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/14ED6FEA-2010-E511-BE3F-782BCB6E0A6D.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/3AF343D6-2010-E511-A653-0025902008CC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/40CA6612-2110-E511-9EAE-0025905A497A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/4278D74B-2110-E511-9009-003048FFCBFC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/4E9C957D-1A10-E511-827D-002481E94B2A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/5C40B725-2110-E511-8BF5-0025905A6092.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/78B4A0D9-2010-E511-B3AF-E41D2D08E090.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/8426B5E7-2010-E511-95FD-0025905A6132.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/86A4472A-2110-E511-9B61-0025905A48C0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/94BC3222-2210-E511-BF30-3417EBE64C09.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/9A478CD9-2010-E511-8D1B-E41D2D08DF60.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/9EFF5215-2110-E511-9D0C-0025905964CC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/A23B022B-2110-E511-B971-0025905B8598.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/BC0E741E-1A10-E511-96E9-002590AC4C72.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/CEA07328-2110-E511-98BC-0025905A6092.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/D2A037E3-2010-E511-B329-0025905A48F0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/D667903C-2110-E511-96AA-003048FFD7D4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/E2611BE8-2010-E511-AEF9-0025905A60B0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/EC459516-2110-E511-ACBB-0025905B855C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/70000/ECE36435-2110-E511-9099-0025905A6060.root' ] );


secFiles.extend( [
               ] )


