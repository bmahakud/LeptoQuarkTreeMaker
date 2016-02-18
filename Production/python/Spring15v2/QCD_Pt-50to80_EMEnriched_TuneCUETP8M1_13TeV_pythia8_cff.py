import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0AE021A1-3207-E511-B1BC-0025905A6122.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1897032E-3107-E511-AFE2-0025905A608A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1CBF45AF-3207-E511-8865-0025905A608A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/20FB2648-8608-E511-9FE9-002481E154CE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2214862E-3107-E511-A3E7-0025905A48C0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/269AEF30-3107-E511-8926-0025905A609E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2E13BC2E-3107-E511-B126-0025905A60BC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/32EAD894-0007-E511-B4BD-002590AC50C2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3400872F-3107-E511-BEB1-0025905A6068.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3AF85098-B907-E511-AE37-3417EBE5281F.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3EFCBA2E-5C07-E511-898F-0002C92A1024.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4CDE409C-B907-E511-B8A8-7845C4FC3A16.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/506DC09D-3207-E511-89CE-0025905964A6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/54B1BB2E-3107-E511-B694-0025905A60BC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5E2151FB-8508-E511-825F-C4346BB25698.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5E9DEBAE-6707-E511-9812-AC853D9DAD0D.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/62601130-3107-E511-8738-0025905A609E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/64003CA3-3207-E511-B6CE-00259059642E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/74DD159B-3207-E511-A879-002590593876.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7E7FF6DD-6707-E511-9DA8-842B2B298D13.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/90A3EBF2-E106-E511-A711-0025904C5180.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9E507A31-3107-E511-94DD-0025905B8590.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A828DC96-B907-E511-86E0-3417EBE6470E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B2763199-B907-E511-A5C9-7845C4FC3C7D.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/BAB4CF4F-0607-E511-8A5C-00259073E4E6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/C6982903-6807-E511-85CD-AC853D9DAC29.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/CCDB0527-0107-E511-A08D-003048F0E1EA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/CE25A761-0607-E511-BF62-00259073E4F6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/DC0FBC33-3107-E511-85C0-0025905A60E4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/DEA56695-B907-E511-B64D-3417EBE645A9.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/DEA6BE45-0607-E511-BF39-00259073E412.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/E038C331-3107-E511-815B-0025905A6118.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FC94872C-3107-E511-8B74-0025905A60C6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/00990E0B-C807-E511-942C-3417EBE6475F.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/00A07D25-E207-E511-9642-008CFA0518D4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/06CF7411-6C06-E511-83B9-00259073E384.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/081CD6FE-C707-E511-B2DC-00A0D1EE26D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/08492621-E207-E511-A98B-6CC2173BBA40.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/08D75038-8607-E511-9116-002590DB9286.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/0A687A53-DA08-E511-8BC0-002590593920.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/0C67175B-8607-E511-BBDE-00266CF32AF4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/102D585D-E207-E511-888C-AC162DACC3F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1204C94F-E207-E511-A6A6-00266CFFBDAC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/12751CAC-F208-E511-A985-AC162DACC3F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/16527BF8-E006-E511-BC9C-0025904C516C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/186C1230-C807-E511-A52E-F04DA275C03D.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1A4CD34A-E207-E511-8897-C4346BB236C0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1CBE7147-E806-E511-B0E0-0025905C9724.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1CC4964C-6D06-E511-BFBB-00259074AE98.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1CF3725A-8507-E511-8264-002590DB923C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1E5B6C8A-8406-E511-929D-00259073E4CC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1EB7EEB1-6F06-E511-ACEE-00259074AE82.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/227D16E2-AA08-E511-9CE6-002481E0DAB0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/246433E6-AA08-E511-B014-047D7BD6DE60.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/2E119588-3509-E511-A28B-782BCB281FC8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/2E9C053E-8607-E511-8BC5-002590A2CCF2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/2EC2E00A-E106-E511-BCD9-0025905C96EA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/30168B48-E906-E511-90CD-0025905C96EA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/30ECF217-6E06-E511-BF88-00259073E35A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/32587653-DA08-E511-AFA2-0025905A60B0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/32DAA9CE-6F06-E511-AD5D-00259073E35A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/3885B08E-7F06-E511-A03A-002590747DDC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/3A3C4062-8507-E511-9BD0-002590D57E3C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/3C82A1C2-6608-E511-87C8-AC853D9DACE5.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/3CE8CB5C-E207-E511-A1AB-00266CFFCB28.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/3E28FE65-E207-E511-9EB5-AC162DAB0B08.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/3E4B8596-2107-E511-ACE5-0025905AA9F0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/442EC51F-E207-E511-9735-C4346BC8E730.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/447E2348-6C06-E511-866B-00259074AE3E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/4861A08A-7F06-E511-8455-00259073E438.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/4A07721A-C507-E511-AAAC-3417EBE6475F.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/4AF980C5-6F06-E511-932F-00259074AE3E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/4CBB878B-E207-E511-A124-AC162DABAF78.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/4E9C51E6-E006-E511-8548-0025905C3D3E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/50FF8D47-E806-E511-AD85-0025904C540C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/5296F29C-2107-E511-977E-0025905B8606.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/54F4FCF4-C707-E511-A55E-3417EBE2F4B1.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/5A90B03B-8607-E511-9DA1-00266CFFA204.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/5AFA6A3E-C807-E511-A9B6-7845C4F8AF24.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/5E3FF763-A908-E511-828B-002590A36084.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/5E7B8FB8-9B06-E511-B7F4-00261894393B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/623BE5C9-9806-E511-B6F3-002618943947.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/64086B38-8C09-E511-9243-001E67397B25.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/6683662C-E106-E511-BF59-0025905C3DCE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/68241E48-E806-E511-9CE0-0025904C6622.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/685B614A-6C06-E511-B38E-00259073E510.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/6C2475C0-8F09-E511-81EB-00266CFABAF0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/6EDC8B88-EA06-E511-ABE8-0025905C96EA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/765E6C75-E207-E511-9AC9-AC162DABCAF8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/76A71348-6C06-E511-9950-00259074AE5C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/78651DCD-6D06-E511-A5CE-00259073E384.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/7877B456-8106-E511-8848-00259073E3C8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/7A5326DD-C707-E511-A18F-7845C4FC346A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/824AC253-6C06-E511-8B95-00259073E35A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/82E86AE3-E006-E511-BB62-0025905C95F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/84E2435C-E207-E511-8CF1-6CC2173BC850.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/8623694E-E806-E511-90C4-0025904CF75A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/88F99747-E207-E511-AE90-6CC2173BC990.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/8A1A1CCD-9806-E511-AF03-0026189438C4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/8C0CB4EA-E307-E511-8C1B-0025905C95FA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/900A30EE-E006-E511-BC6B-0025905C3D6C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/9085FBE4-8407-E511-98FE-002590A36084.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/94C6943C-8607-E511-9970-00266CF33340.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/A81957CF-9806-E511-8B27-0025905A611E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/AA9FC4F4-C707-E511-BFBD-848F69FD2F64.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/AE7E49CF-6608-E511-886E-000F5327373C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/B007525C-E207-E511-A96F-6CC2173BC1D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/B0884EFB-8407-E511-B6B6-002590DB924E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/B0B70247-E806-E511-858F-003048947BBB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/B2AB5301-C807-E511-B2C0-3417EBE64501.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/B47F62CA-9806-E511-A40B-00261894393B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/B65F20E6-C707-E511-88A4-3417EBE64BA3.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/BAB847C9-9806-E511-971D-00248C0BE012.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/BC026C9D-7206-E511-8B82-00259073E53C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/BC03CC8E-7407-E511-BF92-0025905B8590.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/BE6B7747-E806-E511-84EB-0025904C66EA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/BE78D93E-8607-E511-B0D4-002481E10D3E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/C01BB958-E207-E511-88E2-6CC2173BBEC0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/C630A0E2-AA08-E511-BA9C-00266CFFA2C4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/C6D0008D-7F06-E511-AC22-002590574A44.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/CA27DC45-8507-E511-BBD5-002590DB91F0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/CA2A2F4D-7E06-E511-BBDB-00259073E442.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/CA4519CE-9806-E511-B440-003048D15DE4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/CA8CCAE9-AA08-E511-84D1-00266CF32E70.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/CC983807-6E06-E511-A615-00259074AE3E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/CED780A1-6608-E511-BDB7-00259074AEA6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/D007E400-C807-E511-8BD2-3417EBE643DE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/D0DE8847-E806-E511-A9FC-0025904C5180.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/D0F05D8D-7F06-E511-B61A-00259073E442.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/D0F0C91E-6E06-E511-A4ED-00259074AE5C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/D87488FF-6F06-E511-B432-00259074AE5C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/DC0ED53E-8607-E511-81A7-047D7B881D0C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/DE32C93D-8607-E511-B213-002481E0D5E2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E06B2676-E207-E511-B11A-6CC2173BB900.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E2AF393E-6D06-E511-AE4E-00259073E3FC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E40069CA-6608-E511-9C30-842B2B2924F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E808D5E3-E006-E511-82DE-0025905C96A6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F29B5297-2107-E511-A1AD-0025905A6056.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F2DCA3E5-C707-E511-A600-7845C4FC3A2B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F4125067-8507-E511-9BF5-002590AC4C76.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F4238F0F-E207-E511-A568-C4346BBCB6A8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F6118835-E207-E511-B1AD-C4346BC8F6D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F8BC7F45-E806-E511-B28A-0025904CF93C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/FC3D9E47-E806-E511-BFC3-0025905C96EA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/FEF5EC43-E207-E511-827A-6CC2173BC060.root' ] );


secFiles.extend( [
               ] )

