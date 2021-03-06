import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/0C0243DB-EEFD-E411-85E7-AC853D9F52D8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/0C745748-38FD-E411-8FD4-0025905C2CE4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/10B5F390-31FD-E411-9613-0025905A60A0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/120ADEC7-E1FC-E411-AA30-00259073E4FC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/129EFAE0-3FFD-E411-AC33-002590FC5ACC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/1AF2C9F0-E1FC-E411-BE54-00259073E4B6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/1E63133E-44FD-E411-A9F7-0025907DC9F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/40307FE9-E2FD-E411-9C4B-0025904C66F6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/4203A181-31FD-E411-82BA-0025905964C4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/46A2E495-31FD-E411-BC00-0025905964A6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/4A98EE22-41FD-E411-95E7-6CC2173BB980.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/7CD5BBB6-52FD-E411-B7AF-0025905A609E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/88C2B5AC-32FD-E411-A48F-0025905B85F6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/9061B3AD-6FFC-E411-A560-0025905B85D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/AAF038F3-E1FC-E411-B82E-00259073E3CE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/B25DE4AE-32FD-E411-AD92-0025905A60F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/BE51939E-01FE-E411-BAC6-000F530E4784.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/CC3CA08D-4EFD-E411-9ED3-001E673969FA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/CCF503E9-3FFD-E411-87B2-001E673970C1.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/FA4B5A81-31FD-E411-BFE3-002590593920.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/04946C03-60FC-E411-8317-0025905C2CBC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/0675BF0C-E5FB-E411-9FA4-0025905A605E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/068C9E5E-60FC-E411-97EB-002590A82B8E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/0C0ACFC6-E4FB-E411-B4F1-0025905822B6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/12E967CB-E4FB-E411-BCFC-002618943954.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/14DAFD6B-EDFB-E411-8BE5-00259073E3D2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/14F04A72-60FC-E411-A773-0025904B1370.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/222D0C6B-60FC-E411-BBB3-842B2B185C3B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/24FDE75A-E6FB-E411-B2CA-0025905A605E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/2618AD1C-60FC-E411-9F6B-0025905C3D3E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/2C6A26A4-E4FB-E411-9E89-002618943954.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/3A31D308-E5FB-E411-8AF4-0025905964B6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/3E4B5F79-60FC-E411-B540-782BCB281FC8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/446EE6EC-5FFC-E411-83AA-0026189438F5.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/56BDE90D-E5FB-E411-A29E-0025905A6088.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/60280A66-EDFB-E411-84C6-002590D0AFF4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/7CB2ECE2-5FFC-E411-9F9D-002590574A44.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/844E9358-E6FB-E411-B4F4-002618943981.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/8C7D056C-60FC-E411-A1D8-001E688651D4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/9014090D-E5FB-E411-A0F9-0025905B8592.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/92558261-60FC-E411-B876-00266CFADEC0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/92601505-60FC-E411-94CF-002354EF3BDF.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/92C289F6-E3FB-E411-AC10-003048FFCB74.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/9C4B9B16-60FC-E411-8BE3-0025905C2CD2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/A436A77A-EEFB-E411-ACD5-002590D0AF4C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/B8727670-60FC-E411-A655-047D7B881DAE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/CE164A6F-60FC-E411-ACD5-002590A37116.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/EC466FF2-5FFC-E411-8B1A-1CC1DE1D1F80.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/FACA6C43-EEFB-E411-8AB0-00259073E3C0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1A248B68-D2FB-E411-88A3-003048FFD736.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1CE79620-DBFB-E411-9A9F-0025B3E063B4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/22104196-D2FB-E411-AF51-002590D0AF92.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/28CC1E2F-DBFB-E411-AE4F-001E67397D91.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4AD540EC-DAFB-E411-8E6B-002590593902.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4C262352-DBFB-E411-9E5E-002590147CA2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4C4DD8FD-DAFB-E411-9C66-002590AC4BF6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/689B2249-DBFB-E411-BADA-047D7BD6DDB2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7017F90C-DBFB-E411-852A-0025905A6132.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/76A14003-DBFB-E411-BB26-782BCB6E13BB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/809C0D05-D0FB-E411-9DD1-52540049CF9E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A8138DEA-DAFB-E411-BD7C-C4346BBCB6A8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/AA4BB230-DBFB-E411-86C8-0025904C6788.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B6E5722E-DBFB-E411-A82C-0025904C6224.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D03ADDFF-DAFB-E411-9174-B083FED76D99.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/E6997513-D3FB-E411-8570-00261894387E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F667FEEA-DAFB-E411-B56C-B083FED73FEC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/0CD5BBF7-B5FB-E411-93C8-00259073E322.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/16D63A31-B6FB-E411-A8A2-0025905C4300.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/188B9EF3-B5FB-E411-83D6-00259073E532.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1AF31C56-B6FB-E411-986B-002590494E34.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/2E07EC18-B6FB-E411-94A6-0025905A6136.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/3832E5FE-B5FB-E411-8867-000F53273500.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/38A6865C-B6FB-E411-8EEF-002590200B00.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/46454717-B6FB-E411-BBE1-0025905A6060.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/48B75D0A-B6FB-E411-BE2A-002618943833.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/4ED98C0D-B6FB-E411-8450-001E67397D00.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/50C56F14-B6FB-E411-9FB1-0025905A612C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/5263D4EC-B5FB-E411-AB75-0025905C94D2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/584779EA-B5FB-E411-B9AE-002590775016.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/625E48E6-B5FB-E411-8688-00259073E316.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/6C2B8D1F-B6FB-E411-8E36-0025904C66F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/6E0BC9F2-B5FB-E411-B940-002590747D94.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/8E012959-B6FB-E411-BC4B-0025B3E05CDA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/90742B2D-B6FB-E411-82B8-002590200ABC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/9AA4EFE8-B5FB-E411-9FAC-525400E604B7.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/A89A2C07-B6FB-E411-B7BB-0025905C4262.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/ACA3F85F-B6FB-E411-9BA5-1CC1DE1D1F80.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/B27C4246-B6FB-E411-9EFC-0025905C42F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/BEF2BCF4-B5FB-E411-888B-000F53273734.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/C2E3C451-B6FB-E411-94AD-0025905C3DD0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/D026104C-B6FB-E411-B38D-0025B31E3C00.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/D8A3BCF7-B5FB-E411-8182-782BCB6E13BB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/EE475B58-B6FB-E411-B66A-002481E0E440.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/0020CA5C-49FC-E411-828E-002590A2CCE6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/04EA122F-D9FB-E411-947D-0025905B860C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/0A442600-49FC-E411-BA30-0025905A6094.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/0A8C45F9-D9FB-E411-84AF-003048FFD754.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/1842BF00-49FC-E411-83FC-0025905A6094.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/308ADFF8-48FC-E411-8470-00266CFADEC0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/34AE2B25-DBFB-E411-BD43-0025905964B4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/38E0F5F8-D9FB-E411-940D-0026189438F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/3A5F472B-DAFB-E411-B319-002618FDA287.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/4690BC65-DEFB-E411-B01B-00259073E32A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/4CEE147C-DEFB-E411-94FB-0025907B4F1C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/4CEFB179-DEFB-E411-9D36-002590D0B020.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/5A04CE10-49FC-E411-B906-002590A80E0A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/623AF147-D9FB-E411-8A37-002354EF3BE1.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/625BC658-45FC-E411-887A-001E6865A599.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/7E0EFE4A-D9FB-E411-B35B-0025905B85A2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/805734D0-45FC-E411-81F3-842B2B298D13.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/864B0B6F-49FC-E411-A8DF-003048F0E82C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/988C4CF9-48FC-E411-BBB0-00259074AE94.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/989B0086-49FC-E411-B0EC-0025904C4F50.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/9C2CA5E4-42FC-E411-BBC8-6CC21739CEE0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/B03AD315-49FC-E411-9D27-002481E75CF0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/BA8186C9-45FC-E411-B1CA-842B2B1858FB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/C6154F85-49FC-E411-A4D1-0025904CDDEC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/E6BAD485-49FC-E411-A34F-0025904B7C42.root' ] );


secFiles.extend( [
               ] )


