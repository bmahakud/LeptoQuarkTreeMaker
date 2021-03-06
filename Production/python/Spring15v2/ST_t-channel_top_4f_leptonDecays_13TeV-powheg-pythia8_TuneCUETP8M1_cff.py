import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/548FB0B9-D072-E511-84CA-0025908653C4.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/C0B71BB5-D072-E511-9033-00304865C456.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/C6ED97B6-D072-E511-93C3-90B11C267182.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/CEDC33B5-D072-E511-B90E-0CC47A13CC7E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/02E2870B-5F74-E511-AB6B-0CC47A6C1866.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/0445A278-6374-E511-A55D-0025901D1668.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/04F63381-6374-E511-8AC5-0025901D08E4.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/14FAEEE2-6474-E511-8889-0CC47A13D418.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/18AEAD86-6374-E511-9487-002590488694.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/1E644AEE-6174-E511-AAD2-90B11C2CC96F.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/203CD90A-5F74-E511-907C-0CC47A6C1402.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/20EF3466-6374-E511-8C24-0025908217DA.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/24895A84-6374-E511-B110-0CC47A13CDB0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/2A1AF6E9-6174-E511-9834-90B11C27F610.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/2A2B027B-6374-E511-A375-00259048B754.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/32359FFA-6174-E511-BF94-002590488694.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/3289CD8B-5D74-E511-94FF-00304865C254.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/32AD1FFB-5E74-E511-B133-003048344C22.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/34A88F15-5F74-E511-B349-0025901D08E6.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/3C033AF1-6174-E511-B682-0025901D08E8.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/3E5912EE-6174-E511-B4AF-00238B8A3CEE.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/3E829C7F-6374-E511-B9A3-003048F59728.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/400FE4E8-6474-E511-BC66-90B11C2CC96F.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/441E71F1-6174-E511-AA93-002590E3A224.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/46740AF1-6174-E511-AE36-00259048BF92.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/46C97F93-6374-E511-BDA9-90B11C2CC96F.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/4CD51776-6374-E511-B509-003048344A90.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/5047B9FB-6174-E511-8F7A-90B11C26815F.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/54413FF0-6174-E511-88B2-0CC47A13CB62.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/5625718B-6374-E511-9632-0025904AC2C4.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/56EF467D-6374-E511-93DF-00259084A6C4.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/582BAAFE-5E74-E511-887F-002590725380.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/5831FCF6-5E74-E511-AB1F-00304865C4A2.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/58C79D74-6374-E511-B5CB-003048F59728.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/5A1AA1FD-5E74-E511-B31F-002590E2D9FE.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/60FF25EF-6174-E511-8E9B-00304865C466.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/62EFD690-6374-E511-9D2A-002590CB0B5A.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/6425B07A-6374-E511-85B1-003048F5B69E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/64D7C1FC-5E74-E511-BA8F-00238BBD758E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/682AF577-6374-E511-925C-0025901D08B0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/6E1F1007-5F74-E511-89EA-0025907253C6.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/6EAF6705-6574-E511-B5A5-003048F5B2A0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/7ED6AC0C-5F74-E511-BC19-003048F7CC92.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/845AE379-6374-E511-A615-0025904A8ECA.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/84FF71ED-6174-E511-BA94-0CC47A13CCFC.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/8632EAFC-5E74-E511-B74C-0CC47A6C17FC.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/8681910B-5F74-E511-934C-002590E3A222.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/8A0066F5-5E74-E511-8767-0CC47A13D052.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/8C016903-5F74-E511-921B-00304865C45A.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/8E647173-6374-E511-BE15-0CC47A13CB36.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/8EA63879-6374-E511-AF72-002590491B22.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/94735697-6374-E511-B16D-0CC47A13D0BC.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/94B003F3-5E74-E511-AD79-90B11C2ACF20.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/96B38CEE-6174-E511-BFB1-90B11C27F8B2.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/98E35F79-6374-E511-B8AA-90B11C26815F.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/9E1EC2F0-6174-E511-B1B4-0CC47A13CDB0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/9E509594-6374-E511-8439-0CC47A13CC7A.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/9E73A501-5F74-E511-9560-0CC47A13CB18.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/9E90C302-5F74-E511-A38C-0CC47A13CD56.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/A0E23795-6374-E511-9920-002590E3A0D4.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/A6B93C63-6374-E511-9135-90B11C27F89E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/B28385F0-6174-E511-8A51-0025901D1668.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/B2F4CEEF-6174-E511-8A99-002590491B22.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/B6E966F3-5E74-E511-B550-002590E2DD10.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/C2E353F3-6174-E511-9861-90B11C2AA430.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/CE591190-5D74-E511-9473-003048344C22.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/D2D5C8FC-5E74-E511-927B-0CC47A6C1034.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/D4CFD076-6374-E511-B7BC-0CC47A13D176.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/D6823B8A-5D74-E511-8F16-003048F5ADF8.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/D8FD0B92-5D74-E511-A429-003048F5B2F0.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/DA9860EC-6174-E511-A9BD-0CC47A13D284.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/DCE6F479-6374-E511-91E2-00304865C466.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/DEE0A9E0-6474-E511-8AB3-0CC47A13CEAC.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/E078890D-5F74-E511-A4C9-002590E2F664.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/E0C6C0E1-6474-E511-A819-90B11C27E141.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/E46BE48F-5D74-E511-9052-00238BBD7584.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/E63B13EF-6174-E511-852C-0025908217DA.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/EAAFBCEB-6174-E511-AE82-002590E39F2E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/EE070F04-5F74-E511-B187-00238BCE463E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/F0D47502-6274-E511-B307-003048F5B69E.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/FA1305EE-6174-E511-9C7B-0CC47A13CCFC.root',
       '/store/mc/RunIISpring15MiniAODv2/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/80000/FC3EEA06-5F74-E511-8AB6-0CC47A13CECE.root' ] );


secFiles.extend( [
               ] )

