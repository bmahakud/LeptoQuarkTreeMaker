import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/584/00000/960C6DB2-855D-E511-8D34-02163E014535.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/587/00000/8697FF2E-925D-E511-AA26-02163E011D97.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/629/00000/5ADCA5C0-085F-E511-9BC0-02163E014541.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/630/00000/E0C781DC-265F-E511-BBC2-02163E0143A4.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/662/00000/464D55C9-F35E-E511-986B-02163E01454B.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/672/00000/3CDD7DCE-EF5E-E511-8747-02163E014234.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/673/00000/0CEB188B-195F-E511-8A2F-02163E013716.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/674/00000/00DDD980-F05E-E511-8FEF-02163E0145B9.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/675/00000/BC2B27A5-A55F-E511-89A9-02163E0144C3.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/676/00000/18EF2F6A-3B5F-E511-82B0-02163E014329.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/676/00000/ACF2AB06-8B5F-E511-8BDE-02163E0145E4.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/676/00000/DCBCF116-8B5F-E511-A25F-02163E0134FE.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/676/00000/E48851F2-8A5F-E511-A4BE-02163E0146C7.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/677/00000/5037A2D8-435F-E511-8404-02163E014312.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/677/00000/5EF0A4E6-435F-E511-9DE3-02163E014422.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/721/00000/4E81A8E3-085F-E511-B46F-02163E012861.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/725/00000/6AE4E9DD-205F-E511-90C2-02163E011A43.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/727/00000/E44BB517-3F5F-E511-92E1-02163E01190B.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/728/00000/3E1502AC-3A5F-E511-A040-02163E014267.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/729/00000/14D5B80C-0060-E511-B777-02163E014750.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/729/00000/26E7B914-0060-E511-B168-02163E017131.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/729/00000/2EF3680B-0060-E511-8C0C-02163E0121D3.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/729/00000/320AAC5F-8A5F-E511-B05B-02163E01214D.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/729/00000/82D3120A-0060-E511-81A7-02163E014234.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/729/00000/CEE93D09-0060-E511-85DA-02163E0146D2.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/734/00000/98D8F57D-DE5F-E511-B085-02163E0133C8.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/798/00000/A6411DFB-B35F-E511-BEBE-02163E0139A8.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/801/00000/4672E317-F15F-E511-A43F-02163E013857.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/834/00000/642F19E4-FF5F-E511-93A6-02163E0138BD.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/842/00000/A8AAE084-5060-E511-A154-02163E01345C.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/843/00000/080436E6-7561-E511-990C-02163E014208.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/843/00000/4EEBD6C1-9E61-E511-98FC-02163E011B7B.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/843/00000/6ACAA9CC-8461-E511-ABDF-02163E01466E.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/843/00000/863BFCA1-8461-E511-91D4-02163E0146E7.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/843/00000/9AD46996-D560-E511-9844-02163E011AC2.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/865/00000/90FAB9AF-F060-E511-8688-02163E014720.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/866/00000/12B367C5-FC60-E511-AB46-02163E0128A4.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/867/00000/5E709235-1C61-E511-BFD7-02163E01393A.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/868/00000/72B30D31-8561-E511-9B81-02163E01461B.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/868/00000/ECE986E0-8861-E511-BB1C-02163E0144CD.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/869/00000/32C10E84-1861-E511-8BC0-02163E013557.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/924/00000/3C9CC7C1-5F61-E511-B0B7-02163E0133A4.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/925/00000/50B38D2F-6561-E511-96EB-02163E011B36.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/926/00000/BEAEF8D8-DC66-E511-A4F8-02163E01342B.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/935/00000/28006B40-9D61-E511-A61D-02163E013454.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/936/00000/0A26FF1B-2F62-E511-B918-02163E0142B3.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/936/00000/36FC9A23-2F62-E511-AC0D-02163E013520.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/936/00000/4073511E-2F62-E511-BFEF-02163E011E2A.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/936/00000/5CDEE11A-2F62-E511-B317-02163E014526.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/936/00000/64C04711-2F62-E511-B41A-02163E014229.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/936/00000/9C2D1517-2F62-E511-AD62-02163E01469A.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/936/00000/9E1C5D15-2F62-E511-9356-02163E014237.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/936/00000/A6D4C537-2F62-E511-8FA9-02163E01422D.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/936/00000/DE751F82-2F62-E511-A0DC-02163E014510.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/256/941/00000/60F60193-1162-E511-8EE0-02163E0141DA.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/024/00000/B6DCE2A7-2562-E511-946F-02163E013514.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/027/00000/3AEBA0F6-3062-E511-B4B2-02163E0135AC.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/394/00000/2268769F-2D64-E511-A0D8-02163E01434F.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/395/00000/5A167796-1864-E511-8C6C-02163E01434F.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/397/00000/D6A5911D-4364-E511-A86F-02163E011A3F.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/398/00000/7EB69F90-3164-E511-AB57-02163E012B2E.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/399/00000/042E916F-6364-E511-9629-02163E011D19.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/399/00000/300CA056-6364-E511-A146-02163E011D19.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/400/00000/389C4E24-0365-E511-A33B-02163E0138B2.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/400/00000/5E6B3D22-0365-E511-9E5A-02163E011B06.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/400/00000/AE3B7C22-0365-E511-A470-02163E01299A.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/400/00000/DC90D022-0365-E511-9F9A-02163E01434F.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/400/00000/F200211F-0365-E511-8E79-02163E0144C5.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/460/00000/1E56601D-DB64-E511-8022-02163E014316.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/461/00000/9A7F5DA1-2C65-E511-9BD2-02163E014321.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/487/00000/CA51FCB8-6866-E511-9592-02163E01469B.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/487/00000/FE482049-9E65-E511-9F26-02163E0119FD.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/490/00000/FCDAC3DD-4366-E511-9AA5-02163E013787.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/529/00000/EC772A68-CB65-E511-9D36-02163E01430E.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/531/00000/DEF66C0E-0366-E511-A1BC-02163E011C53.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/598/00000/EE740188-2A66-E511-B409-02163E0133D5.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/599/00000/18CF47E2-6466-E511-9112-02163E0138B9.root',
       '/store/data/Run2015D/HTMHT/MINIAOD/PromptReco-v3/000/257/611/00000/3A012ABC-6366-E511-AE89-02163E014235.root' ] );


secFiles.extend( [
               ] )

