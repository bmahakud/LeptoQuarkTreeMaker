import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/02A417B0-9D03-E511-AA88-549F35AD8BFD.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/1A71D4B3-9D03-E511-A099-0025905B855C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/1CAE1F72-A503-E511-8319-549F358EB7A3.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/2AC0F1B4-9D03-E511-8590-0025905A48F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/4085FBB6-9D03-E511-A0BF-008CFA1983E0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/42A6898D-9D03-E511-9096-842B2B182385.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/4AE9ADAF-9D03-E511-A81C-549F358EB721.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/5010739A-9D03-E511-B9DD-549F358EB755.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/60620FB5-9D03-E511-805C-0025905A60D2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/7AEFD7C2-9D03-E511-A5C2-842B2B2B0EC5.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/84FD40B5-9D03-E511-A57D-0025905A6070.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/9A422CB5-9D03-E511-A567-549F35AD8B7B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/A6FB76AF-9D03-E511-AA89-549F35AD8BC9.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/AA2526B4-9D03-E511-A1BD-0025905A6122.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/B09A76B1-9D03-E511-BF6A-3417EBE480D1.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/E8ED46B5-9D03-E511-BF78-0025905A60D2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/ECA874B4-9D03-E511-BFDE-0025905A6134.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0208CBF0-7C03-E511-B3AD-00259073E3FC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/062922AB-7D03-E511-9084-0025905A48BC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0C35CAF1-7C03-E511-98B4-008CFA1C64B0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/10F49256-7D03-E511-9BE5-001E688650C4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/142994EF-7C03-E511-9992-0025904A891A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/161024AD-7D03-E511-A220-0025905B860C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/16F74D56-7D03-E511-9867-0025905B85B2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/18218255-7D03-E511-A00E-0025905B85D6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/18FAABF8-7C03-E511-9E1E-003048FFD752.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1A936FFE-7C03-E511-9141-00266CFCCB44.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1CFE09F2-7C03-E511-8D49-549F35AC7DFB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2025F9F5-7C03-E511-B74D-0025905A48BB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/20CCB8EE-7C03-E511-AC7D-0025904A8592.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/24788CF7-7C03-E511-BF07-0025905A48F0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/260664F4-7C03-E511-96FC-0025905A48BC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/26EEE8F0-7C03-E511-9129-008CFA1660F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2E06E0F2-7C03-E511-95F9-008CFA197D98.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3851DF57-7D03-E511-AB54-0025905A60CA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3A548CFB-7C03-E511-8CFE-0025905B8606.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3ECBCCAD-7D03-E511-95EB-0025905A612A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3ECF4EF1-7C03-E511-A2F5-008CFA197B44.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/40859EAC-7D03-E511-AADA-0025905A6060.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/46B7CCC3-7D03-E511-A828-0025905A48D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4E76F51A-7D03-E511-8BA4-00A0D1EEAAF4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4E888EED-7C03-E511-A456-002590D6009C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/506D95F0-7C03-E511-A136-549F35AD8B95.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/521040F6-7C03-E511-B162-0025905B8582.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/528CC4F5-7C03-E511-8851-0025905B8610.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/52A4E9A8-7D03-E511-85F1-0025905A608A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5682AF56-7D03-E511-8335-0025905A48BC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/582D92F4-7C03-E511-9EE8-0025905A6066.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/586004F5-7C03-E511-B7BD-0025905A6070.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5A0652F0-7C03-E511-B520-180373FF94D6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5A0FE4F5-7C03-E511-A9A4-0025905B8562.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5C8FB551-7D03-E511-AF28-782BCB6E134C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/6027C0F6-7C03-E511-9644-00266CFCC9F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/62156A5C-7D03-E511-9EF6-0025905B8606.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/6219D7F5-7C03-E511-A14E-549F35AC7E49.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/64556155-7D03-E511-913C-0025905A60E0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/68F8BBF4-7C03-E511-9B7C-0025905A497A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/6AA314AD-7D03-E511-B0B2-0025905B858A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/705D9459-7D03-E511-81D3-0025905B8576.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7478FFAB-7D03-E511-9F44-0025905A60E0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/76A3AB55-7D03-E511-A58C-0025905A60E0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/76F2DD56-7D03-E511-8863-0025905B860C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7897FBAA-7D03-E511-B9EC-0025905B85D6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/78D01256-7D03-E511-8017-0025905A48F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7C0B9BEE-7C03-E511-A646-0025904AFFCC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7E94E8ED-7C03-E511-ABA3-485B39800B84.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7EE39B9F-7D03-E511-8406-00259059391E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8065C7F5-7C03-E511-A970-0025905A60E0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/808222EC-7C03-E511-B2C9-0CC47A4DEE0A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/82EE9956-7D03-E511-83BC-0025905B8562.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/866983EE-7C03-E511-A93F-3417EBE64699.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A29E2EED-7C03-E511-81DF-549F35AD8BC9.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/AA200FFB-7C03-E511-8B4A-782BCB27BA01.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/AA8E1996-7D03-E511-9AE8-0025905B8562.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/AACEADEF-7C03-E511-A919-848F69FD4EDD.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/ACB70FAC-7D03-E511-9463-0025905A60D2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B0BEB857-7D03-E511-9348-0025905B8610.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B2693AAB-7D03-E511-AB88-0025905A60F8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B4FD38F9-7C03-E511-9806-001E6878FB39.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B82400F8-7C03-E511-AEA6-782BCB6A50CA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B8508AF6-7C03-E511-A124-008CFA06477C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/BECECEF6-7C03-E511-A8F2-001E688629D2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/C0D614F7-7C03-E511-9402-008CFA056400.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/C4AC12F7-7C03-E511-A856-0025905B8576.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/C619DFF2-7C03-E511-944F-008CFA14FA8C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/C8149355-7D03-E511-8E18-001E688651D4.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/CA7746F7-7C03-E511-967E-B499BAA2AC54.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/CEC1E054-7D03-E511-A983-0025905A6066.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/CEC97CF2-7C03-E511-9FE1-848F69FD29B2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D2189AEB-7C03-E511-B99E-0025907B4F6C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/DCB823F4-7C03-E511-982D-008CFA56D794.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/E4DCD259-7D03-E511-943B-00259059391E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/E66B47F5-7C03-E511-AFDF-0025905A48D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/ECEAF1ED-7C03-E511-AACF-0025907B4EC0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/EE2344AB-7D03-E511-97EF-0025905A48F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FC9B9655-7D03-E511-B59A-0025905A610C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FCD338F4-7C03-E511-A4E7-782BCB407EDE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FCED31F5-7C03-E511-9634-0025905A48F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/148C0F8F-B303-E511-9D91-782BCB40899C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1ADA628D-B303-E511-8D2B-0025905A48EC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/1C42F4ED-BB03-E511-A6B1-008CFA051614.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/2C110B83-B303-E511-BDF2-0025905C2CA6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/3230339A-B303-E511-A0E1-008CFA580730.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/387A848F-B303-E511-A047-0025905B85EE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/3AECB38C-B303-E511-8819-0025905A48D0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/42A4F567-B303-E511-8877-B083FED7593B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/442061B6-BC03-E511-8FF2-008CFA064778.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/5629FC95-B303-E511-ACA4-549F35AD8B61.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/5A127D8C-B303-E511-AA7E-0025905A60D2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/5E9B5775-B303-E511-B760-3417EBE6450D.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/60CA768E-B303-E511-B804-0025905B860C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/6C2F618D-B303-E511-9716-00259055C994.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/6EA41094-B303-E511-9B8F-0025905B85B2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/7272485D-B303-E511-9FA2-52540001DACD.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/785CEC96-B303-E511-B7CF-549F35AF4517.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/84123690-B303-E511-970A-0025905964C2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/8693DE87-B303-E511-AE26-00259055CA34.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/94359995-B303-E511-9424-0025907FD280.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/96DC0A94-B303-E511-8B43-0025905B8590.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/96E96793-B303-E511-A924-0025905B861C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/9A75FA39-B303-E511-8617-525400B401A9.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/A08EB2A0-BB03-E511-98BE-549F358EB7BD.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/D0587898-B303-E511-8FAE-549F35AF44D6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E0D3DDED-B303-E511-9154-0025905B85F6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E842E682-B303-E511-9BB2-0025905C2CA6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E884FE8C-B303-E511-A69C-0025905B859E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/EE110B84-B303-E511-8B45-0025901D493A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F0336E89-B303-E511-9092-782BCB6A5183.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F6567E8C-B303-E511-9C75-0025905A606A.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F8806795-B303-E511-81B4-0025905B85AE.root' ] );


secFiles.extend( [
               ] )

