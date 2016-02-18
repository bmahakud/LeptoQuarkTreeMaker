import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/0AF8E723-53F9-E411-86B4-0025905C2CBA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/12621BBA-53F9-E411-8492-0025904CF766.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/20BB04BA-53F9-E411-9CEF-0025904C68D8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/2C4C5151-1DFA-E411-9804-0025905C2CE6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/3E9DFDEC-3FFA-E411-BDE5-20CF3027A631.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/40A870F8-13FA-E411-BFFD-0025907FD430.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/66A1DA7F-54F9-E411-984B-0025905C2CBA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/66C0A199-4AF9-E411-AFD6-0026B92E24A7.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/7CF1C9D4-3FFA-E411-81CE-002590A80E1C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/920C042C-19FA-E411-B60E-00266CFFCB14.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/969D1683-52F9-E411-B4CC-0025904C6216.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/9CC1E7F0-42FA-E411-8C86-00266CF9B3FC.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/A88292F9-E5F9-E411-90D1-002618943874.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/B4173132-13FA-E411-84F6-842B2B185AAA.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/CE39E729-A2F9-E411-AECF-E0CB4E29C4F6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/CE9AA33E-34F9-E411-B05C-00259073E3FE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/ECF36155-29F9-E411-A5B3-002590D0AF54.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/1CEF760B-DDF9-E411-8EA2-842B2B2925F5.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/2E314C0F-DDF9-E411-9175-6CC2173BBA60.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/50902203-DDF9-E411-8FCC-003048FFD756.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/7A3A7D06-DDF9-E411-AEF0-0025905B85EE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/7A8F623F-DDF9-E411-BED9-0025B3E05C24.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/82242CFC-DCF9-E411-9A97-00259074AE3E.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/B098210F-DDF9-E411-B328-00215AEDFD12.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/B283C807-DDF9-E411-B038-000F530E4AB0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/B86D7349-DDF9-E411-A09D-0025904C66F2.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/B8BD8D0C-DDF9-E411-888E-0025907DCA64.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/DE151309-DDF9-E411-B0E0-842B2B298D0B.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/E4D9F41A-1FFA-E411-8DC9-00266CFADEC0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/E6F1BFE0-4CF9-E411-B56D-00259074AE80.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/009D5085-FBFA-E411-A6D2-00259073E456.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1EB41976-9EFA-E411-9032-AC853D9DACD7.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/28DFDF1C-A7FA-E411-A941-00266CFFBE68.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2C38E2AB-5AF9-E411-89CE-002590747DF0.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/301F1F9B-14FB-E411-BDB4-0026B92E0ED7.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/36598081-14FB-E411-BC03-782BCB239FB6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/56F9A4BF-B0FA-E411-86FD-002590A80E1C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/60611C71-A6FB-E411-9BD4-00266CFFA68C.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/668CD402-05FA-E411-9814-0025905C2CA6.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7AFD147D-4DF9-E411-8694-20CF305B0501.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8EB30379-14FB-E411-81AB-AC853D9DAC19.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/98A7E07E-A6FB-E411-B291-00215AD4D6AE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9E71FA75-9EFA-E411-B681-B083FED76508.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A07BC41B-23FA-E411-B437-485B39800BAB.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B0AA0B84-D4FA-E411-930D-0025905B8606.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/E4E6B379-9EFA-E411-B5DA-AC853D9DAC41.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FE7B30AA-48F9-E411-93D0-002590D0B004.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/50B99FBD-AEF9-E411-8612-000F53273498.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/545EA050-BDF9-E411-8EDB-782BCB407EDE.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/62D746C2-AFF9-E411-9CDF-AC853D9F5256.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/6A9761FA-BCF9-E411-AB34-000F53273498.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E4367A30-AFF9-E411-861F-0026B92E24A7.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/E89C4B14-BDF9-E411-9A0A-002590D0B086.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/EA1B109C-BDF9-E411-A4F6-0025905C3DF8.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/F60E66FC-BCF9-E411-BA85-AC853DA06A54.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/FC0BB383-AEF9-E411-8CB4-001E68865390.root',
       '/store/mc/RunIISpring15DR74/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/50BF4983-57F9-E411-B82D-20CF3027A630.root' ] );


secFiles.extend( [
               ] )


