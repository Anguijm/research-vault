---
type: reference
study: world-class-planning
title: QVD field inventory — every table and field in the operator's Qlik environment
classification: internal
created: 2026-07-27
generated_from: 01_sources/qlik/QLIK Data Dictionary.xlsx (1,180 field rows, 50 QVDs)
---

# QVD field inventory

Every table and field available in the Qlik environment, generated from the operator's
data dictionary so we stop guessing at field names. Three schemas: **AIM** (planning and
scheduling, 482 fields), **COST** (actual expended labor and financials, 405), and **MAT**
(material, 293).

Regenerate with the script noted at the bottom if the dictionary is refreshed.

## How the tables link (the `%` key fields)

These are the association keys. A key appearing in two QVDs is the join between them;
that is the fastest way to see which links are actually available.

| Key field | Appears in |
|-----------|------------|
| `%Act_Matl_Key` | `AIM_JML`, `AIM_Matl_Hist` |
| `%Act_Proj_Key` | `AIM_CuPhase`, `AIM_Key_Event_And_Milestones`, `AIM_Project` |
| `%BBJS_FO05_FM40_Key` | `COST_BBJS_SUM`, `COST_FO05_FM40` |
| `%BBJS_SAFR_KEY` | `COST_BBJS_SUM` |
| `%BBJS_TSD_Key` | `COST_BBJS_SUM` |
| `%BBJS_XREF_Key` | `COST_BBJS_SUM`, `COST_BEA_BESA_JNLU_XREF` |
| `%Ctcod_Key, //Key to FM25 tabl` | `COST_FS10` |
| `%Ctcod_Key,//Key to FS10 Tabl` | `COST_FM25` |
| `%CuPh_TaskSerial_Key` | `AIM_Task`, `AIM_Task_Hist` |
| `%CuPhase_Component_Key` | `AIM_Component_NUC` |
| `%CuPhase_Key` | `AIM_Component`, `AIM_Component_Assy_NUC`, `AIM_CuPhase`, `AIM_CuPhase_Hist`, `AIM_FCN_CU_PHASE`, `AIM_Instruction`, `AIM_JCN`, `AIM_JML`, `AIM_SWLIN`, `AIM_TEST_RQMT`, `AIM_Task` |
| `%Cu_Phase_MAT_Key` | `AIM_CuPhase`, `MAT_Materials` |
| `%Effcd_Clcde_Joser4_Kopcd_Kowkt_Key` | `COST_FE75`, `COST_FE77` |
| `%FA05_MAT_Key` | `COST_FA05`, `MAT_Materials` |
| `%FCN_SWLIN_Key` | `AIM_FCN_SWLIN`, `AIM_SWLIN` |
| `%FH05_MAT_Key` | `COST_FH05`, `MAT_Materials` |
| `%FJ90_FE75_Key, //Same key to FJ90 and FJ7` | `COST_FE75` |
| `%FM40_FJ77_Key` | `COST_FJ77`, `COST_FO05_FM40` |
| `%FO05_FA05_Key` | `COST_FA05`, `COST_FO05` |
| `%FO05_FH05_Key` | `COST_FH05`, `COST_FO05` |
| `%FO05_FJ40_Key` | `COST_FJ40`, `COST_FO05_FM40` |
| `%FO05_FM40_Key` | `COST_FO05` |
| `%Fdfdn_Key,//Key to FF10 and FF40 table` | `COST_FF05` |
| `%ICNKOP_KEY` | `COST_FE05`, `COST_Overhead_JON_Ref` |
| `%JCN_Key` | `AIM_JB_JCN`, `AIM_JCN`, `AIM_JCN_Addition` |
| `%JML_Matl_Status_Key` | `AIM_JML` |
| `%JON_KEY` | `COST_Direct_Line_Item_Ref`, `COST_FE05`, `COST_FJ90`, `COST_Overhead_JON_Ref` |
| `%JO_CuPhase_Key` | `AIM_CuPhase` |
| `%JobSumm_CuPhase_Key` | `AIM_CuPhase`, `AIM_JobSummary_CuPhase` |
| `%JobSumm_SWLIN_Key` | `AIM_JobSummary_SWLIN`, `AIM_SWLIN` |
| `%KE_Ref_Key` | `AIM_Key_Event_And_Milestones` |
| `%M02_M03_Key` | `MAT_Materials` |
| `%M03_M04_Key` | `MAT_Materials` |
| `%M04_M05_Key` | `MAT_Materials` |
| `%M05_M10_Key` | `MAT_Materials` |
| `%M10_M102_Key` | `MAT_Materials` |
| `%M10_M11_Key` | `MAT_Materials` |
| `%M10_M12_Key` | `MAT_Materials` |
| `%M10_M14_Key` | `MAT_Materials` |
| `%M10_M23_Key` | `MAT_Materials` |
| `%M10_M30_Key` | `MAT_Materials` |
| `%M10_M32_Key` | `MAT_Materials` |
| `%M32_M230_Key` | `MAT_Materials` |
| `%M35_M30_Key` | `MAT_Materials` |
| `%PTS_TDM_KEY` | `MAT_Trigger_Materials` |
| `%Package_Key` | `AIM_CuPhase`, `AIM_Package` |
| `%Proj_Ship_Key` | `AIM_Project`, `AIM_Ship`, `AIM_Work_Order` |
| `%SWLIN_LI_CU_Phase_Key` | `AIM_SWLIN` |
| `%SWLIN_LI_KEY` | `AIM_SWLIN` |
| `%Ship_JB_JCN_Key` | `AIM_JB_JCN`, `AIM_Ship` |
| `%Shnbr_Key` | `COST_FS10` |
| `%Shnbr_Key, //Key to FS1` | `COST_FJ40` |
| `%TDM_TD_Key` | `MAT_Trigger_Materials` |
| `%Tracking_Doc_M14_Key` | `MAT_Trigger_Materials` |
| `%WLR_Key` | `COST_BBJS_SUM` |
| `%Wkccd_Cowke_Joser_Shnbr_Key, //Same Key needs to be put in FJ41 and FJ4` | `COST_FJ40` |
| `%Wkccd_Cowke_Key` | `COST_FO05` |
| `%XREF_TSD_Key` | `COST_BEA_BESA_JNLU_XREF` |
| `%socc_tran_jnlu_xref_Key` | `COST_BEA_BESA_JNLU_SOCC_TRAN`, `COST_BEA_BESA_JNLU_XREF` |

---

# AIM schema

## `AIM_Component.qvd`  (19 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPhase_Key` | ACTIVITY_SA_ID, COMP_SA_ID |  |
| `CU Date` | CREATE_DT | Create Date is the date the component was created. |
| `CU Type` | COMP_TYPE_CD | Component (CU) Type refers to the code that denotes the name of the component unit.  ex: V- (Valve) |
| `Comp Assy Name` | COMP_ASSY_NM |  |
| `Component Activity ID` | ACTIVITY_SA_ID |  |
| `Component Name` | COMP_NM | Component Name refers to the standard name for a component unit. ex: valve |
| `Component Name` | COMP_NM | Component Name refers to the standard name for a component unit. ex: valve |
| `Component desc` | DESC_TX | Description is the narrative description for the component unit. |
| `Fbw Scs CD` | FBW_SCS_CD | Identification code for the Fly-By-Wire Ship Control System certification boundary (FBW SCS). |
| `Level One` | LEVEL_ONE_FLAG_CD | The Level One flag identifies the component as a MIC level component (as oppose to Standard level).  Note: "Level" refers to the level of control nece |
| `Nuclear` | NUC_FLAG_CD | The Nuclear flag identifies the component as a nuclear COMPONENT_NEW. |
| `PLANT_NUM_ID` | PLANT_NUM_ID | The Plant Number (or Plant ID) refers to the numerical designator of the machinery space to which the component is associated. |
| `PLANT_NUM_ID1` | DESC_TX | Description is the narrative description for the component unit. |
| `SFCC CD` | SFCC_CD | Identification code for the Submarine Flight Critical Component certification boundary (SFCC). |
| `Security Level ID` | SECURITY_LEVEL_ID | Security level breakdown for space access based on security levels assigned to components. |
| `Space CD` | SPACE_CD | Space refers to the set of characters that denotes a compartment on a ship. |
| `Subsafe` | SUBSAFE_FLAG_CD | The Subsafe flag identifies the component as a Submarine Safe COMPONENT_NEW. |
| `Zone ID` | ZONE_ID |  |
| `component.mod_dt` | MOD_DT | Mod Date is the date the component was modified. |

## `AIM_Component_Assy.qvd`  (1 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `Comp Assy Name` | COMP_ASSY_NM |  |

## `AIM_Component_Assy_NUC.qvd`  (9 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPhase_Key` | ACTIVITY_SA_ID, COMP_ASSY_SA_ID |  |
| `Comp Assy Name` | COMP_ASSY_NM |  |
| `Comp Assy SFCC` | SFCC_CD | Identification code for the Submarine Flight Critical Component certification boundary (SFCC). |
| `Comp Assy Security Level` | SECURITY_LEVEL_ID | Security level breakdown for space access based on security levels assigned to components. |
| `Comp Assy Space` | SPACE_CD | Space refers to the set of characters that denotes a compartment on a ship. |
| `Comp Assy Subsafe` | SUBSAFE_FLAG_CD |  |
| `CompAssy.Comp_type_cd` | COMP_TYPE_CD | Component (CU) Type refers to the code that denotes the name of the component unit.  ex: V- (Valve) |
| `Nuc Flag Cd` | NUC_FLAG_CD |  |
| `comp_assy.mod_dt` | MOD_DT | Modify Date |

## `AIM_Component_NUC.qvd`  (16 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPhase_Component_Key` | ACTIVITY_SA_ID, COMP_SA_ID | Component identifier |
| `CU Date` | CREATE_DT | Create Date is the date the component was created. |
| `CU Type` | COMP_TYPE_CD | Component (CU) Type refers to the code that denotes the name of the component unit.  ex: V- (Valve) |
| `Component Activity ID` | ACTIVITY_SA_ID |  |
| `Component Name` | COMP_NM | Component Name refers to the standard name for a component unit. ex: valve |
| `Component desc` | DESC_TX | Description is the narrative description for the component unit. |
| `Fbw Scs CD` | FBW_SCS_CD | Identification code for the Fly-By-Wire Ship Control System certification boundary (FBW SCS). |
| `Level One` | LEVEL_ONE_FLAG_CD | The Level One flag identifies the component as a MIC level component (as oppose to Standard level).  Note: "Level" refers to the level of control nece |
| `NUC_FLAG_CD` | NUC_FLAG_CD | The Nuclear flag identifies the component as a nuclear COMPONENT_NEW. |
| `PLANT_NUM_ID1` | PLANT_NUM_ID | The Plant Number (or Plant ID) refers to the numerical designator of the machinery space to which the component is associated. |
| `SFCC CD` | SFCC_CD | Identification code for the Submarine Flight Critical Component certification boundary (SFCC). |
| `Security Level ID` | SECURITY_LEVEL_ID | Security level breakdown for space access based on security levels assigned to components. |
| `Space CD` | SPACE_CD | Space refers to the set of characters that denotes a compartment on a ship. |
| `Subsafe` | SUBSAFE_FLAG_CD | The Subsafe flag identifies the component as a Submarine Safe COMPONENT_NEW. |
| `Zone ID` | ZONE_ID | Zone refers to a 5 digit numeric code that identifies an area or location of work that is standard for a physical location within a class of ships. |
| `component.mod_dt` | MOD_DT | Mod Date is the date the component was modified. |

## `AIM_CuPhase.qvd`  (70 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Act_Proj_Key` | ACTIVITY_SA_ID, PROJ_ID |  |
| `%CuPhase_Key` | ACTIVITY_SA_ID, COMP_ASSY_SA_ID |  |
| `%CuPhase_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID |  |
| `%CuPhase_Key` | ACTIVITY_SA_ID,NET_NODE_ID |  |
| `%Cu_Phase_MAT_Key` | ACTIVITY_SA_ID, ICN, KO |  |
| `%JO_CuPhase_Key` | ACTIVITY_SA_ID, JOB_ORDER_SA_ID |  |
| `%JO_CuPhase_Key` | ACTIVITY_SA_ID,  JOB_ORDER_SA_ID |  |
| `%JobSumm_CuPhase_Key` | ACTIVITY_SA_ID, ICN |  |
| `%Package_Key` | ACTIVITY_SA_ID, PACKAGE_SA_ID |  |
| `ACTUAL_COMPLETION_DATE` | ACC_DT |  |
| `ACTUAL_COMPLETION_DATE_EMPTY` | ACC_DT |  |
| `ACTUAL_START_DATE` | ACS_DT |  |
| `ACTUAL_START_DATE_EMPTY` | ACS_DT |  |
| `BPC_DT` | BPC_DT |  |
| `BPS_DT` | BPS_DT |  |
| `CALENDAR_ID` | CALENDAR_ID |  |
| `COAR` | WORK_CAT_CD & AVAIL_ID |  |
| `CU Phase Activity ID` | ACTIVITY_SA_ID |  |
| `CU Phase Serial` | CU_PHASE_SERIAL_ID | the serial identifier used to identify next available KO |
| `CURRENT_COMPLETION_DATE` | STC_DT | the date that denotes performance early finish date |
| `CURRENT_START_DATE` | STS_DT | the date that denotes performance early start date |
| `CU_PHASE_BAIM_FromDate` | CU_PHASE_BAIM_FromDate |  |
| `CU_PHASE_BAIM_ToDate` | CU_PHASE_BAIM_ToDate |  |
| `CU_PHASE_REMARKS` | REMARKS_TX | the text that denotes user remarks |
| `CU_PHASE_SA_ID` | CU_PHASE_SA_ID | System assigned identifier for CU Phases. |
| `CU_WORK_CAT_CD` | WORK_CAT_CD | the code that denotes work category codes for funding purposes |
| `CU_swlin_sys_id` | SWLIN_SYS_ID | the identifier that denotes the SWLIN system identifier |
| `Comp Assy Name` | COMP_ASSY_NM |  |
| `Comp Assy SFCC` | SFCC_CD | Identification code for the Submarine Flight Critical Component certification boundary (SFCC). |
| `Comp Assy Security Level` | SECURITY_LEVEL_ID | Security level breakdown for space access based on security levels assigned to components. |
| `Comp Assy Space` | SPACE_CD | Space refers to the set of characters that denotes a compartment on a ship. |
| `Comp Assy Subsafe` | SUBSAFE_FLAG_CD |  |
| `CompAssy.Comp_type_cd` | COMP_TYPE_CD | Component (CU) Type refers to the code that denotes the name of the component unit.  ex: V- (Valve) |
| `Cu Phase Comp Name` | COMP_NM | the name of the component or assembly |
| `Cu Phase Duration QY` | DURATION_QY | the quantity that denotes duration for work |
| `Cu Phase Est Resolution Date` | EST_RESOLUTION_DT | the date that denotes estimated date of resolution |
| `Cu Phase Group CD` | GROUP_CD | the code that denotes opportunity window group |
| `Cu Phase Prepared by Date` | PREPARED_BY_DT |  |
| `Cu Phase Project ID` | PROJ_ID | the identifier for the availability (proj_id and avail_id are synonymous) |
| `Cu Phase Title` | TITLE_TX | the text that denotes the CU Phase title |
| `Float Type Cd` | FLOAT_TYPE_CD |  |
| `ICN` | ICN | the internal control number for a CU Phase |
| `ICN_KO` | ICN, KO | the internal control number for a CU Phase and the key operation assignment for a CU Phase |
| `JOBORDER_CD` | JOBORDER_CD |  |
| `JOB_ORDER_BAIM_FromDate` | JOB_ORDER_BAIM_FromDate |  |
| `JOB_ORDER_BAIM_ToDate` | JOB_ORDER_BAIM_ToDate |  |
| `JO_SERIAL_ID` | JO_SERIAL_ID | Job Order Enclosure Number |
| `Job Order #` | WORK_CAT_CD & AVAIL_ID & JO_NO_LAST5 |  |
| `Job Order Title` | TITLE_TX |  |
| `KEYOP_CD` | KEYOP_CD |  |
| `KEY_TASK_SERIAL_ID` | KEY_TASK_SERIAL_ID | the identifier for the key task |
| `KO` | KO | the key operation assignment for a CU Phase |
| `MANHOUR_QY` | MANHOUR_QY |  |
| `Nuc Flag Cd` | NUC_FLAG_CD |  |
| `PHASE_REPEAT_QY` | PHASE_REPEAT_QY | the quantity that denotes the repeat of a CU Phase |
| `PROGRESS_RT` | PROGRESS_RT | the rate that denotes percent complete of work |
| `SCHEDULED_COMPLETION_DATE` | STC_DT |  |
| `SCHEDULED_START_DATE` | STS_DT |  |
| `TGI Code` | TGI_RESPONSIBLE_CD | the code that denotes a responsible group or person for an associated TGI |
| `Total Float Qty` | TOTAL_FLOAT_QY |  |
| `WORK_TYPE_CD` | WORK_TYPE_CD | the code that denotes the type of work (ex. O (Original), N (New Work), R (Rework)) |
| `WPC_NOTES_TX` | WPC_NOTES_TX |  |
| `WS_REASON_CD` | WS_REASON_CD | the code that denotes work stoppage status |
| `aps_User_Name` | APS_USER_SA_ID | the identifier that denotes a zone manager |
| `comp_assy.mod_dt` | MOD_DT | Modify Date |
| `create_User_Name` | CREATE_USER_SA_ID | the identifier that denotes the CU Phase creator |
| `cu_phase.mod_dt` | MOD_DT | the date that denotes when a user last modified the row |
| `job_order.mod_dt` | MOD_DT |  |
| `mod_User_Name` | MOD_USER_SA_ID | the quantity that denotes released network float |
| `prepared_by_User_Name` | PREPARED_BY_USER_SA_ID |  |

## `AIM_CuPhase_Hist.qvd`  (12 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPhase_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID |  |
| `Approval Status CD` | APPROVAL_STATUS_CD |  |
| `CU_PHASE_HIST_BAIM_FromDate` | CU_PHASE_HIST_BAIM_FromDate |  |
| `CU_PHASE_HIST_BAIM_ToDate` | CU_PHASE_HIST_BAIM_ToDate |  |
| `CU_PHASE_HIST_SA_ID` | CU_PHASE_HIST_SA_ID |  |
| `Change CD` | CHANGE_CD |  |
| `Cu Hist User SA ID` | USER_SA_ID |  |
| `Cu Phase Hist Activity ID` | ACTIVITY_SA_ID |  |
| `Current Flag Cd` | CURRENT_FLAG_CD |  |
| `Status Change Date` | STATUS_CHANGE_DT |  |
| `Status Set Date` | STATUS_SET_DT |  |
| `Working Status CD` | WORKING_STATUS_CD |  |

## `AIM_FCN_CU_PHASE.qvd`  (8 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPhase_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID |  |
| `CU_PHASE_FCN_FromDate` | CU_PHASE_FCN_FromDate |  |
| `CU_PHASE_FCN_ToDate` | CU_PHASE_FCN_ToDate |  |
| `FCN` | WORK_CAT_CD, PROJ_ID, SWLIN_SYS_ID, SWLIN_SERIAL_ID |  |
| `FCN Prorate Labor Rate` | PRORATE_LBR_RT |  |
| `FCN Prorate Material Rate` | PRORATE_MATL_RT |  |
| `FCN Work Category Code` | WORK_CAT_CD |  |
| `Obsolete Indication` | OBSOLETE__INDICATION |  |

## `AIM_FCN_SWLIN.qvd`  (10 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%FCN_SWLIN_Key` | ACTIVITY_SA_ID, PROJ_ID, SWLIN_SYS_ID, FUND_ACT_ID, SWLIN_SE |  |
| `Control Number Charge Code` | CTRL_NUM_CHARGE_CD |  |
| `FCN` | WORK_CAT_CD, PROJ_ID, SWLIN_SYS_ID, SWLIN_SERIAL_ID |  |
| `FCN Project ID` | PROJ_ID |  |
| `FCN Prorate Labor Rate` | PRORATE_LBR_RT |  |
| `FCN Prorate Material Rate` | PRORATE_MATL_RT |  |
| `FCN Work Category Code` | WORK_CAT_CD |  |
| `FCN_FromDate` | FCN_FromDate |  |
| `FCN_ToDate` | FCN_ToDate |  |
| `Obsolete Indication` | OBSOLETE__INDICATION |  |

## `AIM_Instruction.qvd`  (4 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPhase_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID |  |
| `Due Date` | DUE_DT |  |
| `TGI Change #` | CHANGE_ID |  |
| `TGI Status` | TGI_STATUS_CD |  |

## `AIM_JB_JCN.qvd`  (38 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%JCN_Key` | ACTIVITY_SA_ID, JCN_SA_ID | JCN_SA_ID: Indicates jcn_addition JCN_SA_ID |
| `%Ship_JB_JCN_Key` | ACTIVITY_SA_ID, UNIT_ID_CD | UNIT_ID_CD: Indicates jcn UNIT ID CD |
| `ACTION_TAKEN_STATUS_NM` | ACTION_TAKEN_STATUS_NM | contains the full status name |
| `APL_AEL_CD` | APL_AEL_CD | Indicates jcn APL_AEL_CD |
| `BROKER_FUND_ACT_CD` | BROKER_FUND_ACT_CD |  |
| `CASREP_CAT_CD` | CASREP_CAT_CD |  |
| `CASREP_DATE_TIME_GRP_TXT` | CASREP_DATE_TIME_GRP_TXT |  |
| `CDMDOA_RIN_ID` | CDMDOA_RIN_ID | CDMDOA component record identification number |
| `DEADLINE_DT` | DEADLINE_DT | Indicates jcn_addition DEADLINE_DT |
| `EQUIP_ID_CD` | EQUIP_ID_CD | Indicates jcn UNIT ID CD |
| `EQUIP_NOUN_NM` | EQUIP_NOUN_NM | Indicates jcn EQUIP_NOUN_NM |
| `EQUIP_SERIAL_NUM_ID` | EQUIP_SERIAL_NUM_ID | Indicates jcn EQUIP_SERIAL_NUM_ID |
| `EST_MAN_DAY_COST_QY` | EST_MAN_DAY_COST_QY | Indicates jcn EST_MAN_DAY_COST_QY |
| `EST_MATERIAL_COST_QY` | EST_MATERIAL_COST_QY | Indicates jcn EST_MATERIAL_COST_QY |
| `EST_TOTAL_COST_QY` | EST_TOTAL_COST_QY | Indicates jcn_addition EST_TOTAL_COST_QY |
| `FIRST_CONTACT_MAN_NM` | FIRST_CONTACT_MAN_NM | Indicates jcn FIRST_CONTACT_MAN_NM |
| `FUND_ACT_CD` | FUND_ACT_CD | SWLIN FAC |
| `INITIAL_CASREP_CD` | INITIAL_CASREP_CD |  |
| `JB_JCN` | JOB_SEQUENCE_NUM_ID | Indicates jcn JOB SEQUENCE NUM ID |
| `JB_JCN Avail ID` | AVAIL_ID | Indicates jcn AVAIL_ID |
| `JB_JCN CSMP_NM` | CSMP_NM | Indicates jcn CSMP_NM |
| `JB_JCN Est Man Days Qy` | EST_MAN_DAYS_QY | Indicates jcn EST_MAN_DAYS_QY |
| `JB_JCN Location ID` | LOCATION_ID | Indicates jcn JOB SEQUENCE NUM ID |
| `JB_JCN Received Date` | RECEIVED_DT | Indicates jcn RECEIVED_DT |
| `JB_JCN Remarks Desc` | REMARKS_DESC_TX | Indicates jcn REMARKS_DESC_TX |
| `JB_JCN SWLIN LI ID` | SWLIN_LI_ID | Identifies the SWLIN Line Item |
| `JB_JCN SWLIN LI TX` | SWLIN_LI_TX | SWLIN Line Item text |
| `JB_JCN Ship Board Wrk Ctr Cd` | SHIP_BOARD_WRK_CTR_CD | Indicates jcn SHIP BOARD WRK CTR CD |
| `JCN_DESC_TX` | JCN_DESC_TX |  |
| `JCN_PRIORITY_CD` | JCN_PRIORITY_CD | Indicates jcn JCN_PRIORITY_CD |
| `JCN_REVIEW_CD` | JCN_REVIEW_CD | Indicates jcn JCN REVIEW CD |
| `SECOND_CONTACT_MAN` | SECOND_CONTACT_MAN | Indicates jcn_addition SECOND_CONTACT_MAN |
| `SHIP_SYS_ID` | SHIP_SYS_ID | Identifies Ship system ID |
| `STATUS_CD` | STATUS_CD | Indicates jcn_addition STATUS_CD |
| `SWLIN_SYS_ID` | SWLIN_SYS_ID | Indicates jcn SWLIN_SYS_ID |
| `TYCOM_SCREENING_CD` | TYCOM_SCREENING_CD | Indicates jcn_addition TYCOM_SCREENING_CD |
| `TYPE_AVAILABLE_CD` | TYPE_AVAILABLE_CD | Indicates jcn_addition TYPE_AVAILABLE_CD |
| `UNIT_ID_CD` | UNIT_ID_CD |  |

## `AIM_JCN.qvd`  (24 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPhase_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID | CU Phase Identifier |
| `%JCN_Key` | ACTIVITY_SA_ID, JCN_SA_ID | Job Control Number identifier |
| `%JCN_Key` | ACTIVITY_SA_ID, JCN_SA_ID | Job Control Number Identifier |
| `%JCN_Key` | ACTIVITY_SA_ID, JCN_SA_ID | Job Control Number Identifier |
| `CSMP Summary` | CSMP_NM | The Current Ship's Maintenance Project Name (or Summary) is used to give a brief description of the problem. |
| `JC2` | UNIT_ID_CD, SHIP_BOARD_WRK_CTR_CD, JOB_SEQUENCE_NUM_ID | The Unit Identification Code identifies the yard that is responsible for a repair. |
| `JCN Activity ID` | ACTIVITY_SA_ID |  |
| `JCN Availability` | AVAIL_ID | Availability identifier |
| `JCN Hist Avail` | AVAIL_ID |  |
| `JCN Hist Mod DT` | MOD_DT |  |
| `JCN Hist Mod Reason` | MOD_REASON_CD |  |
| `JCN Hist Type CD` | JCN_TYPE_CD |  |
| `JCN Hist WorkFlow CD` | WORK_FLOW_CD |  |
| `JCN Status` | STATUS_NM | Identifies the Status Type Name |
| `JCN Status CD` | STATUS_CD |  |
| `JCN Status CD` | STATUS_CD | Identifies the Status Type Code |
| `JCN Status Type` | STATUS_TYPE_CD | Identifies the Status Type Code |
| `Job Control Number` | UNIT_ID_CD, SHIP_BOARD_WRK_CTR_CD, JOB_SEQUENCE_NUM_ID | The Unit Identification Code identifies the yard that is responsible for a repair. |
| `REPAIR_ACTIVITY_UIC_ID` | REPAIR_ACTIVITY_UIC_ID |  |
| `Received Date` | RECEIVED_DT |  |
| `Remarks Desc Text` | REMARKS_DESC_TX | Job Control Number Remarks/Description |
| `Tycom Remarks Text` | TYCOM_REMARKS_TX |  |
| `Work Flow Cd` | WORK_FLOW_CD |  |
| `jcn.mod_dt` | MOD_DT | Date record was created or last modified |

## `AIM_JCN_Addition.qvd`  (8 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%JCN_Key` | ACTIVITY_SA_ID, JCN_SA_ID | Job Control Number identifier |
| `CASREP_SERIAL_ID` | CASREP_SERIAL_ID |  |
| `JCN Deadline Date` | DEADLINE_DT |  |
| `JCN Deferral Date` | DEFERRAL_DT |  |
| `JCN Rate CD` | RATE_CD |  |
| `Management Remarks` | COMMENTS_TX |  |
| `SECOND_CONTACT_MAN` | SECOND_CONTACT_MAN |  |
| `TYPE_AVAILABLE_CD` | TYPE_AVAILABLE_CD |  |

## `AIM_JML.qvd`  (29 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Act_Matl_Key` | ACTIVITY_SA_ID, MATL_SA_ID |  |
| `%Act_Matl_Key` | ACTIVITY_SA_ID, MATL_SA_ID |  |
| `%Act_Matl_Key` | ACTIVITY_SA_ID, MATL_SA_ID |  |
| `%Act_Matl_Key` | ACTIVITY_SA_ID, MATL_SA_ID |  |
| `%CuPhase_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID |  |
| `%JML_Matl_Status_Key` | ACTIVITY_SA_ID, DOCNO_ID |  |
| `%JML_Matl_Status_Key` | ACTIVITY_SA_ID, JML_DOCNO_IDN |  |
| `Act Qty` | ACTUAL_QY |  |
| `Act UI` | ACTUAL_UI_CD |  |
| `Additional Information` | ADDITIONAL_INFO_TX |  |
| `Assy Dwg Rev Pc` | ASSY_DWG_ID, ASSY_DWG_REV_ID, ASSY_DWG_PC_ID |  |
| `Detailed Dwg Rev Pc` | DET_DWG_ID, DET_DWG_REV_ID, DET_DWG_PC_ID |  |
| `JML Activity ID` | ACTIVITY_SA_ID |  |
| `JML Document Number` | DOCNO_ID |  |
| `JML NIIN` | NIIN_ID |  |
| `JML Noun Name` | NOUN_NM |  |
| `JML REF Cd` | REF_CD |  |
| `JML Unit Price` | ACTUAL_UNIT_PRICE_AM |  |
| `Matl Status - ETD` | EST_TIME_DELV_DT |  |
| `Matl Status - Qty Due` | QTY_DUE_QY |  |
| `Matl Status - Qty Issued` | QTY_ISSUED_QY |  |
| `Matl Status - Qty NRFI` | QTY_NRFI_QY |  |
| `Matl Status - Qty Ordered` | QTY_ORDERED_QY |  |
| `Matl Status - Qty RFI` | QTY_RFI_QY |  |
| `Opt 1` | OPTIONAL_KEY1_ID |  |
| `RDD` | NEED_DT |  |
| `Supplemental Description` | DESCRIPTION_TX |  |
| `Work Type ID` | WORK_AUTH_ID |  |
| `jml_header.mod_dt` | MOD_DT |  |

## `AIM_JobSummary_CuPhase.qvd`  (10 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%JobSumm_CuPhase_Key` | ACTIVITY_SA_ID, ICN |  |
| `Engineering Notes` | ENGINEERING_NOTES_TX |  |
| `JOB_SUMMARY_BAIM_FromDate` | JOB_SUMMARY_BAIM_FromDate |  |
| `JOB_SUMMARY_BAIM_ToDate` | JOB_SUMMARY_BAIM_ToDate |  |
| `Job Summary Activity ID` | ACTIVITY_SA_ID |  |
| `Job Summary Status` | STATUS_CD |  |
| `Job Summary Title` | TITLE_TX |  |
| `Labor Management Reserve Desc` | LBR_RISK_TX |  |
| `Material Management Reserve Desc` | MATL_RISK_TX |  |
| `job_summary.mod_dt` | MOD_DT |  |

## `AIM_JobSummary_SWLIN.qvd`  (10 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%JobSumm_SWLIN_Key` | SWLIN_SYS_ID, FUND_ACT_CD, SWLIN_SERIAL_ID, PROJ_ID, ACTIVIT |  |
| `Engineering Notes` | ENGINEERING_NOTES_TX |  |
| `JOB_SUMMARY_BAIM_FromDate` | JOB_SUMMARY_BAIM_FromDate |  |
| `JOB_SUMMARY_BAIM_ToDate` | JOB_SUMMARY_BAIM_ToDate |  |
| `Job Summary Activity ID` | ACTIVITY_SA_ID |  |
| `Job Summary Status` | STATUS_CD |  |
| `Job Summary Title` | TITLE_TX |  |
| `Labor Management Reserve Desc` | LBR_RISK_TX |  |
| `Material Management Reserve Desc` | MATL_RISK_TX |  |
| `job_summary.mod_dt` | MOD_DT |  |

## `AIM_Key_Event_And_Milestones.qvd`  (24 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Act_Proj_Key` | ACTIVITY_SA_ID, PROJ_ID |  |
| `%Act_Proj_Key` | ACTIVITY_SA_ID, PROJ_ID |  |
| `%KE_Ref_Key` | KE_ID, ACTIVITY_SA_ID | Unique ID for Key Event |
| `%KE_Ref_Key` | KE_ID, ACTIVITY_SA_ID |  |
| `Event Activity ID` | ACTIVITY_SA_ID |  |
| `Event Activity ID` | ACTIVITY_SA_ID |  |
| `Event Actual Date` | ACC_DT |  |
| `Event Actual Date` | ACC_DT |  |
| `Event Desc` | KEY_EVENT_TX | Name of Key Event |
| `Event Desc` | DESC_TX |  |
| `Event Desired Date` | DES_DT |  |
| `Event Desired Date` | DES_DT |  |
| `Event ID` | MILESTONE_ID |  |
| `Event ID` | KE_ID |  |
| `Event Name` | KE_NM | Name of Key Event |
| `Event Name` | MILESTONE_NM |  |
| `Event Proj ID` | PROJ_ID |  |
| `Event Proj ID` | PROJ_ID |  |
| `Event Status` | STATUS_CD |  |
| `Event Status` | STATUS_CD |  |
| `Event Type` | 'MS' |  |
| `Event Type` | 'KE' |  |
| `event.mod_dt` | MOD_DT | date record was created or last modified |
| `event.mod_dt` | MOD_DT |  |

## `AIM_Matl_Hist.qvd`  (6 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Act_Matl_Key` | ACTIVITY_SA_ID, MATL_SA_ID |  |
| `Action` | ACTION_ID |  |
| `Action Date` | ACTION_DT |  |
| `JML Status` | JML_STATUS_CD |  |
| `Matl Hist Activity ID` | ACTIVITY_SA_ID |  |
| `Position` | OWNER_POSITION_CD |  |

## `AIM_Package.qvd`  (5 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Package_Key` | ACTIVITY_SA_ID, PACKAGE_SA_ID |  |
| `Package Description` | DESC_TX |  |
| `Package ID` | PACKAGE_SA_ID |  |
| `Package Special Instruction` | SPEC_INSTR_TX |  |
| `Package Status` | PACKAGE_STATUS_CD |  |

## `AIM_Project.qvd`  (79 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Act_Proj_Key` | ACTIVITY_SA_ID, PROJ_ID | Project Identifier |
| `%Act_Proj_Key` | ACTIVITY_SA_ID, PROJ_ID |  |
| `%Act_Proj_Key` | ACTIVITY_SA_ID, PROJ_ID |  |
| `%Proj_Ship_Key` | ACTIVITY_SA_ID, HULL_NUM_ID, SHIP_TYPE_CD |  |
| `` | CONTACT_TYPE_CD |  |
| `AIM_PROJ_FLAG_CD` | AIM_PROJ_FLAG_CD |  |
| `ALT_PROGRESS_CD` | ALT_PROGRESS_CD |  |
| `ALT_PROGRESS_SET_DT` | ALT_PROGRESS_SET_DT |  |
| `AOR` | AOR_NM | Area of Responsibility Name |
| `AOR Activity ID` | ACTIVITY_SA_ID |  |
| `AOR.aps_user_sa_id` | APS_USER_SA_ID | Assistant Project Supervisor User Identifier |
| `AOR.aps_user_sa_id2` | APS_USER_SA_ID2 | Assistant Project Superintendent of AOR. |
| `AOR_BAIM_FromDate` | AOR_BAIM_FromDate |  |
| `AOR_BAIM_ToDate` | AOR_BAIM_ToDate |  |
| `Activity Name` |  |  |
| `Badge Number` | USER_ID |  |
| `Beeper Number` | OFF_DUTY_PHONE_ID | The user's beeper number |
| `COMPLETE_ON_APP_CD` | COMPLETE_ON_APP_CD |  |
| `CORPORATE_FLAG_CD` | CORPORATE_FLAG_CD |  |
| `DEF_CALENDAR_ID` | DEF_CALENDAR_ID |  |
| `DEL_FLAG_CD` | DEL_FLAG_CD |  |
| `DRYDOCK_FLAG_CD` | DRYDOCK_FLAG_CD |  |
| `ETWD_CD` | ETWD_CD |  |
| `EXC_YRD_CD` | EXC_YRD_CD |  |
| `FINMET_ERROR_TX` | FINMET_ERROR_TX |  |
| `FINMET_FLAG_CD` | FINMET_FLAG_CD |  |
| `FIN_PROCESS_NBR` | FIN_PROCESS_NBR |  |
| `FIRST_NM` | FIRST_NM | User First Name |
| `FRE_LOCKED_FLAG` | FRE_LOCKED_FLAG |  |
| `JOB_SUPV_FLAG_CD` | JOB_SUPV_FLAG_CD |  |
| `LAST_DML_SA_ID` | LAST_DML_SA_ID |  |
| `LAST_NM` | LAST_NM | User Last Name |
| `LOCATION_NM` | LOCATION_NM |  |
| `MIDDLE_NM` | MIDDLE_NM | User Middle Name |
| `Name` | LAST_NM, FIRST_NM, MIDDLE_NM, ORG_CD | Organization Code of the user's base organization |
| `ORG_CD` | ORG_CD | Organization Code of the user's base organization |
| `PERSONNEL_FromDate` | PERSONNEL_FromDate |  |
| `PERSONNEL_ToDate` | PERSONNEL_ToDate |  |
| `PLAN_YRD_CD` | PLAN_YRD_CD |  |
| `POSITION_SA_ID` | POSITION_SA_ID |  |
| `PROJECT_STATUS_CD` | PROJ_STATUS_CD | The descriptive name of the status of a project |
| `PROJECT_STATUS_CD` | PROJ_STATUS_CD |  |
| `PROJECT_TYPE_CD` | PROJ_TYPE_CD |  |
| `PROJECT_TYPE_CD` | PROJ_TYPE_CD |  |
| `PROJ_RISK_QY` | PROJ_RISK_QY |  |
| `PROJ_STATUS_NM` | PROJ_STATUS_NM | The descriptive name of the status of a project |
| `PROJ_TYPE_NM` | PROJ_TYPE_NM |  |
| `Personnel Activity ID` | ACTIVITY_SA_ID |  |
| `Personnel.Shop_Cd` | SHOP_CD | The Shop Code the user is assigned to |
| `Project Activity ID` | ACTIVITY_SA_ID |  |
| `Project ID` | PROJ_ID |  |
| `Project Name` | PROJ_NM |  |
| `RANK_ID` | RANK_ID |  |
| `REFRESH_INTERVAL_ID` | REFRESH_INTERVAL_ID |  |
| `REFRESH_OVERRIDE_CD` | REFRESH_OVERRIDE_CD |  |
| `REMARKS_TX` | REMARKS_TX |  |
| `REUSE_CD` | REUSE_CD |  |
| `SALES_EST_AM` | SALES_EST_AM |  |
| `SHYD_RISK_QY` | SHYD_RISK_QY |  |
| `Supervisor CD` | SUPERVISOR_CD | The Shop Code the user's supervisor is assigned to |
| `TIME_FACTOR_QY` | TIME_FACTOR_QY |  |
| `TOC_CD` | TOC_CD |  |
| `TOC_LAST_MSP_EXPORT_DT` | TOC_LAST_MSP_EXPORT_DT |  |
| `TOC_ORIG_BASELINE_CD` | TOC_ORIG_BASELINE_CD |  |
| `TOC_REV_BASELINE_CD` | TOC_REV_BASELINE_CD |  |
| `TOC_SET_DT` | TOC_SET_DT |  |
| `TOC_SET_USER_SA_ID` | TOC_SET_USER_SA_ID |  |
| `TOC_STOP_DT` | TOC_STOP_DT |  |
| `TOC_STOP_USER_SA_ID` | TOC_STOP_USER_SA_ID |  |
| `TRANSACT_CD` | TRANSACT_CD |  |
| `USER_SA_ID` | USER_SA_ID | User Identifier |
| `USER_SA_ID` | USER_SA_ID |  |
| `WEIGHTS_MANUALLY_AUDIT_CD` | WEIGHTS_MANUALLY_AUDIT_CD |  |
| `WEIGHTS_MANUALLY_CD` | WEIGHTS_MANUALLY_CD |  |
| `Work Number` | DUTY_PHONE_ID | Users Duty Phone Number without punctuation |
| `Zone_Manager` | APS_USER_SA_ID | Assistant Project Supervisor User Identifier |
| `aor.mod_dt` | MOD_DT | date record created or modified |
| `personnel.mod_dt` | MOD_DT | Date user information was last updated |
| `project.mod_dt` | MOD_DT |  |

## `AIM_SWLIN.qvd`  (25 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPhase_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID |  |
| `%FCN_SWLIN_Key` | ACTIVITY_SA_ID, PROJ_ID, SWLIN_SYS_ID, FUND_ACT_CD, SWLIN_SE | PROJ_ID:  The ID of the Project this COAR is assigned to,  SWLIN_SYS_ID: the identifier that denotes the SWLIN system identifier |
| `%JobSumm_SWLIN_Key` | SWLIN_SYS_ID, FUND_ACT_CD, SWLIN_SERIAL_ID, PROJ_ID,  ACTIVI | SWLIN System Identifier |
| `%SWLIN_LI_CU_Phase_Key` | ACTIVITY_SA_ID,SWLIN_LI_SA_ID |  |
| `%SWLIN_LI_CU_Phase_Key` | ACTIVITY_SA_ID,SWLIN_LI_SA_ID |  |
| `%SWLIN_LI_KEY` | ACTIVITY_SA_ID, SWLIN_SA_ID | SWLIN unique identifier |
| `%SWLIN_LI_KEY` | ACTIVITY_SA_ID, SWLIN_SA_ID |  |
| `Action Type` | ACTION_TYPE_CD |  |
| `Authorized Assignment` | AUTHORIZED_ASSIGN_TX |  |
| `FAC` | FUND_ACT_CD | Funding Account Code |
| `New Work` | NEW_WORK_CD |  |
| `SSI` | SWLIN_SYS_ID | SWLIN System Identifier |
| `SWLIN Activity ID` | ACTIVITY_SA_ID |  |
| `SWLIN ID` | SWLIN_SYS_ID, FUND_ACT_CD, SWLIN_SERIAL_ID | SWLIN System Identifier |
| `SWLIN Labor Rate` | PRORATE_LBR_RT |  |
| `SWLIN Line Item` | SWLIN_LI_ID | The identifier that denotes the SWLIN Line Item |
| `SWLIN Material Rate` | PRORATE_MATL_RT |  |
| `SWLIN Serial ID` | SWLIN_SERIAL_ID | SWLIN Serial Identifier |
| `SWLIN Sys ID` | SWLIN_SYS_ID | SWLIN System Identifier |
| `SWLIN_LI_BAIM_FromDate` | SWLIN_LI_BAIM_FromDate |  |
| `SWLIN_LI_BAIM_ToDate` | SWLIN_LI_BAIM_ToDate |  |
| `SWLIN_PROJ_RISK_QY` | PROJ_RISK_QY |  |
| `SWLIN_TITLE` | TITLE_TX | Title of SWLIN |
| `Serial ID` | SWLIN_SERIAL_ID | SWLIN Serial Identifier |
| `swlin.mod_dt` | MOD_DT | Date SWLIN was created or last updated |

## `AIM_Ship.qvd`  (19 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Proj_Ship_Key` | ACTIVITY_SA_ID, HULL_NUM_ID, SHIP_TYPE_CD | The number assigned by NAVSEA to uniquely identify a ship within a type of class of ships |
| `%Ship_JB_JCN_Key` | SHIP_TYPE_CD |  |
| `Hull Number` | HULL_NUM_ID |  |
| `NATIONALITY_NM` | NATIONALITY_NM | Refers to the country of the home port |
| `PLAN_YD_CD` | PLAN_YD_CD | The code used to identify a specific planning yard |
| `SHIP_ADDR_ONE_TX` | SHIP_ADDR_ONE_TX | Refers to the specific NAVSEA address assigned to the ship |
| `SHIP_ADDR_TWO_TX` | SHIP_ADDR_TWO_TX | Refers to the specific NAVSEA address assigned to the ship |
| `SHIP_CLASS_ID` | SHIP_CLASS_ID | Identifies the ship class |
| `SHIP_OID` | SHIP_OID |  |
| `Ship Activity ID` | ACTIVITY_SA_ID |  |
| `Ship Class` | SHIP_TYPE_CD | The code used to identify a certain type of navy vessel |
| `Ship Class ID` | SHIP_CLASS_ID | Identifies the ship class |
| `Ship Home` | SHIP_HOME_NM | Includes the city and state of ship |
| `Ship Name` | SHIP_NM | The name of the ship |
| `Ship Type` | SHIP_TYPE_CD | The code used to identify a certain type of navy vessel |
| `Ship UIC` | UNIT_ID_CD | A five digit code that represents a unit within the NAVSEA organization |
| `Ship UIC` | SHIP_CLASS_NM | The name associated with standard ship system |
| `TYPE_COMM_NM` | TYPE_COMM_NM | The name of the type commander |
| `ship.mod_dt` | MOD_DT | date record created or last modified |

## `AIM_TEST_RQMT.qvd`  (9 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPhase_Key` | ACTIVITY_SA_ID |  |
| `RQMT_STATUS_CD` | RQMT_STATUS_CD |  |
| `TEST_RQMT_FromDate` | TEST_RQMT_FromDate |  |
| `TEST_RQMT_ToDate` | TEST_RQMT_ToDate |  |
| `TEST_RQMT_VID` | TEST_RQMT_VID |  |
| `TEST_SERIAL_ID` | TEST_SERIAL_ID |  |
| `TST_RQMT_SHIP_SYS_ID` | SHIP_SYS_ID |  |
| `Test Required` | TEST_RQMT_TX |  |
| `WTR_ID` | WTR_ID |  |

## `AIM_Task.qvd`  (22 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPh_TaskSerial_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID, TASK_SERIAL_ID | System assigned identifier for CU Phases and the serial identifier for task under a CU Phase |
| `%CuPhase_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID | System assigned identifier for CU Phases. |
| `Crew Size` | CREW_SIZE_QY | the quantity representing the crew size number required for a specific task |
| `High RAD Hrs Qty` | HIGH_RAD_HOURS_QY | the quantity that denotes high rad hours |
| `Prorate Flag Cd` | PRORATE_FLAG_CD | Indicates proration |
| `RC Grid ID` | RC_GRID_ID | the identifier that denotes RC Grid |
| `Resource Qty` | RESOURCE_QY | the code that denotes scheduled task level resources |
| `Ship Board Wrk Ctr Cd` | SHIP_BOARD_WRK_CTR_CD | the code that denotes Ship Work Centers |
| `Shop Code` | SHOP_CD | Identifies the Shop. |
| `Shop Code` | SHOP_CD | the code that denotes a Shop |
| `Shop Title` | SHOP_NM | Descriptive name for the Shop. |
| `Shop/TSD` | SHOP_CD & TSD_CD | the code that denotes a Shop and the code that denotes a Trade Skill Designator |
| `TAI_ID` | TAI_ID | Obsolete Field |
| `TS Cd` | TS_CD | the code that denotes a Trade Skill |
| `TSD Cd` | TSD_CD | the code that denotes a Trade Skill Designator |
| `Task #` | TASK_SEQ_ID | Indicates the task sequence number |
| `Task Activity ID` | ACTIVITY_SA_ID | Indicates the task sequence number |
| `Task Name` | TASK_NM | the task name |
| `Task Serial ID` | TASK_SERIAL_ID | the serial identifier for task under a CU Phase |
| `Task Subwork Type Cd` | TASK_SUB_WORK_TYPE_CD | the code that denotes the sub work type of a task |
| `Task Text` | TASK_TX | the task description |
| `Task Work Type Cd` | TASK_WORK_TYPE_CD | the code that denotes work type of a task |

## `AIM_Task_Hist.qvd`  (6 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%CuPh_TaskSerial_Key` | ACTIVITY_SA_ID, CU_PHASE_SA_ID, TASK_SERIAL_ID |  |
| `Best Std Manhour Qty` | BEST_STD_MANHOUR_EST_QY |  |
| `Task Hist Activity ID` | ACTIVITY_SA_ID |  |
| `Task Hist Cur Flag` | CUR_FLAG_CD |  |
| `Task Manhours` | MANHOUR_EST_QY |  |
| `task_hist.mod_dt` | MOD_DT |  |

## `AIM_Work_Order.qvd`  (15 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Proj_Ship_Key` | ACTIVITY_SA_ID, HULL_NUM_ID, SHIP_TYPE_CD |  |
| `LAST_POSSIBLE_START_DT` | LAST_POSSIBLE_START_DT |  |
| `OVER_HEAD` | OVER_HEAD |  |
| `SALES_LBR_DOLLARS` | SALES_LBR_DOLLARS |  |
| `SALES_LBR_HRS` | SALES_LBR_HRS |  |
| `SALES_MATL_DOLLARS` | SALES_MATL_DOLLARS |  |
| `SALES_TOTAL_DOLLARS` | SALES_TOTAL_DOLLARS |  |
| `WORK_ORDER_FromDate` | WORK_ORDER_FromDate |  |
| `WORK_ORDER_ID` | WORK_ORDER_ID |  |
| `WORK_ORDER_SA_ID` | WORK_ORDER_SA_ID |  |
| `WORK_ORDER_ToDate` | WORK_ORDER_ToDate |  |
| `WORK_SCOPE_TX` | WORK_SCOPE_TX |  |
| `Work Order Completion Date` | COMPLETION_DT |  |
| `Work Order Mod Date` | MOD_DT |  |
| `Work Order Title` | TITLE_TX |  |

## `TASk_BAIM.qvd`  (4 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `Cu Phase Title` | TITLE_TX |  |
| `High RAD Hrs Qty` | HIGH_RAD_HOURS_QY | the quantity that denotes high rad hours |
| `RC_GRID_ID1` | RC_GRID_ID | the identifier that denotes RC Grid |
| `TASK_NM1` | TASK_NM | the task name |

---

# COST schema

## `Activity_Ref`  (4 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `RMC_CODE` | RMC_CODE |  |
| `RMC_NAME` | RMC_NAME |  |
| `UIC_I` | UIC_I |  |

## `COST_BBJS_SUM.qvd`  (57 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%BBJS_FO05_FM40_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, BEA_CD, BESA_ID | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, BEA_CD: BUDGET EXECUTION ACTIVITY CODE, and BESA_ID: BUDGET EXECU |
| `%BBJS_SAFR_KEY` | ACTIVITY_SA_ID, FISCAL_YEAR_ID | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID and FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER |
| `%BBJS_SAFR_KEY` | ACTIVITY_SA_ID,FISCAL_YEAR_ID | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER |
| `%BBJS_TSD_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, SOCC_ID | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER and SOCC_ID: SUB-OBJECT CLASS CODE IDENTIFIER |
| `%BBJS_TSD_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, SOCC_ID |  |
| `%BBJS_XREF_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, BEA_CD, BESA_ID, JNLU_ID | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, BEA_CD: BUDGET EXECUTION ACTIVITY CODE, BESA_ID: BUDGET EXECUTION |
| `%WLR_Key` | SOCC_ID |  |
| `%WLR_Key` | WORK_LEAVE_CD | WORK LEAVE CODE |
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `BCN_CD` | BCN_CD | WORK CENTER IDENTIFIER (WCI) CODE |
| `BEA_BESA_JNLU_SOC_RUNNO_INSERT` | BEA_BESA_JNLU_SOC_RUNNO_INSERT |  |
| `BEA_BESA_JNLU_SOC_RUNNO_UPDATE` | BEA_BESA_JNLU_SOC_RUNNO_UPDATE |  |
| `BEA_CD` | BEA_CD | BUDGET EXECUTION ACTIVITY CODE |
| `BESA_ID` | BESA_ID | BUDGET EXECUTION SUB-ACTIVITY IDENTIFIER |
| `BYPASS_ID` | BYPASS_ID | STARS EXP HOURS BYPASS INDICATOR |
| `COMP_ID` | COMP_ID | COMPENSATORY TIME IND |
| `CREATED_DATE_TZ` | CREATED_DATE_TZ | CREATED DATE WITH TIMEZONE |
| `CREATED_USER_SA_ID` | CREATED_USER_SA_ID | CREATED USER SYSTEM ASSIGNED ID |
| `Commitment Amount` | COMMITMENT_AM | COMMITMENT AMOUNT |
| `Commitment Quantity` | COMMITMENT_QY | COMMITMENT QUANTITY |
| `DFLT_MATL_SOCC_ID` | DFLT_MATL_SOCC_ID | DEFAULT MATERIAL SUB-OBJECT CLASS CODE |
| `DFLT_MLC_SOCC_ID` | DFLT_MLC_SOCC_ID | DEFAULT MLC SUB-OBJECT CLASS CODE |
| `Expense Amount` | EXPENSE_AM | EXPENSE AMOUNT |
| `Expense Quantity` | EXPENSE_QY | EXPENSE QUANTITY |
| `FCN_ID` | FCN_ID | FINANCIAL CONTROL JOB ORDER NUMBER |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `GL_G_JO_ID` | GL_G_JO_ID | GL UNGRADED JOB ORDER |
| `GL_U_JO_ID` | GL_U_JO_ID | GL GRADED JOB ORDER |
| `JNLU_ID` | JNLU_ID | JOB ORDER NUMBER LOCAL USE IDENTIFIER |
| `LASTMOD_USER_SA_ID` | LASTMOD_USER_SA_ID | LAST MODIFIED USER SYSTEM ASSIGNED ID |
| `LNB_ID` | LNB_ID | LOANS AND BORROWS ID |
| `Liquidation Amount` | LIQUIDATION_AM | LIQUIDATION AMOUNT |
| `Liquidation Quantity` | LIQUIDATION_QY | LIQUIDATION QUANTITY |
| `MIL_ID` | MIL_ID |  |
| `MLC_GL_ACCT_CD` | MLC_GL_ACCT_CD | MLC GENERAL LEDGER ACCOUNT CODE |
| `MODIFIED_DATE_TZ` | MODIFIED_DATE_TZ | MODIFIED DATE WITH TIMEZONE |
| `NSY_ID` | NSY_ID | NON-SHIPYARD BORROWED IND |
| `OH_JO_ID` | OH_JO_ID | OVERHEAD JOB ORDER ID |
| `OH_KO_ID` | OH_KO_ID | OVERHEAD KEYOP ID |
| `Obligation Amount` | OBLIGATION_AM | OBLIGATION AMOUNT |
| `Obligation Quantity` | OBLIGATION_QY | OBLIGATION QUANTITY |
| `PREM_ID` | PREM_ID | PREMIUM ID |
| `SOCC_ID` | SOCC_ID | SUB-OBJECT CLASS CODE IDENTIFIER |
| `SRI_CD` | SRI_CD | SUB-ALLOTMENT RECIPIENT IDENTIFER (SRI) AAC |
| `ST_OT_HOL_ID` | ST_OT_HOL_ID | STRAIGHT/OVERTIME/HOLIDAY ID |
| `Statistical Amount` | STATISTICAL_AM | STATISTICAL AMOUNT |
| `Statistical Quantity` | STATISTICAL_QY | STATISTICAL QUANTITY |
| `TSD SOCC ID` | SOCC_ID | SUB-OBJECT CLASS CODE |
| `TSD Shop CD` | SHOP_CD | SHOP NUMBER CODE |
| `USER_UPD_ID` | USER_UPD_ID | USER UPDATE ID |
| `WCI_CD` | WCI_CD | WORK CENTER IDENTIFIER (WCI) CODE |
| `WLR_SA_ID` | WLR_SA_ID | WORK LEAVE REF SYSTEM ASSIGNED ID |
| `WORK_LEAVE_CD` | WORK_LEAVE_CD | WORK LEAVE CODE |
| `WORK_LEAVE_ID` | WORK_LEAVE_ID | WORK LEAVE ID |
| `WORK_LEAVE_NM` | WORK_LEAVE_NM | WORK LEAVE NAME |
| `WORK_LEAVE_REF_OID` | WORK_LEAVE_REF_OID |  |

## `COST_BEA_BESA_JNLU_SOCC_TRAN.qvd`  (15 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%socc_tran_jnlu_xref_Key` | BEA_CD, BESA_ID, JNLU_ID, FISCAL_YEAR_ID | BEA_CD: BUDGET EXECUTION ACTIVITY CODE, BESA_ID: BUDGET EXECUTION SUB-ACTIVITY IDENTIFIER, JNLU_ID: JOB ORDER NUMBER LOCAL USE IDENTIFIER and FISCAL_Y |
| `ACRN_ID` | ACRN_ID | ACCOUNTING CLASSIFICATION REFERENCE NUMBER ID |
| `COMMITMENT_AM` | COMMITMENT_AM | COMMITMENT AMOUNT |
| `Created` | CREATED_DATE_TZ | CREATED DATE WITH TIMEZONE |
| `DOC_ID_CD` | DOC_ID_CD | DOCUMENT IDENTIFIER CODE (DIC) |
| `Document` | STD_DOC_ID | STANDARD DOCUMENT NUMBER (SDN) ID |
| `EXPENSE_AM` | EXPENSE_AM | EXPENSE AMOUNT |
| `OBLIGATION_AM` | OBLIGATION_AM | OBLIGATION AMOUNT |
| `Qty` | STATISTICAL_QY | STATISTICAL QUANTITY |
| `SOCC_ID` | SOCC_ID | SUB-OBJECT CLASS CODE IDENTIFIER |
| `Socc Tran Fiscal Year` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `Transaction Date` | MODIFIED_DATE_TZ | MODIFIED DATE WITH TIMEZONE |
| `bea_besa_jnlu_socc_tra Activity ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `msm_issued_stat_amt` | STATISTICAL_AM | STATISTICAL AMOUNT |
| `transferred_amt_from_88msm` | LIQUIDATION_AM | LIQUIDATION AMOUNT |

## `COST_BEA_BESA_JNLU_XREF.qvd`  (21 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%BBJS_XREF_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, BEA_CD, BESA_ID, JNLU_ID | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, BEA_CD: BUDGET EXECUTION ACTIVITY CODE, BESA_ID: BUDGET EXECUTION |
| `%XREF_TSD_Key` | ACTIVITY_SA_ID, FCN_ID, SHOP_CD | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FCN_ID: FINANCIAL CONTROL JOB ORDER NUMBER, and SHOP_CD: SHOP NUMBER CODE |
| `%socc_tran_jnlu_xref_Key` | BEA_CD, BESA_ID, JNLU_ID, FISCAL_YEAR_ID | BEA_CD: BUDGET EXECUTION ACTIVITY CODE, BESA_ID: BUDGET EXECUTION SUB-ACTIVITY IDENTIFIER, JNLU_ID: JOB ORDER NUMBER LOCAL USE IDENTIFIER and FISCAL_Y |
| `BEA_CD` | BEA_CD | BUDGET EXECUTION ACTIVITY CODE |
| `BESA_ID` | BESA_ID | BUDGET EXECUTION SUB-ACTIVITY IDENTIFIER |
| `COAR` | FCN_ID | FINANCIAL CONTROL JOB ORDER NUMBER |
| `CREATED_DATE_TZ` | CREATED_DATE_TZ | CREATED DATE WITH TIMEZONE |
| `CREATED_USER_SA_ID` | CREATED_USER_SA_ID | CREATED USER SYSTEM ASSIGNED ID |
| `EXPFUNC` | FCN_ID | FINANCIAL CONTROL JOB ORDER NUMBER |
| `FCN` | FCN_ID | FINANCIAL CONTROL JOB ORDER NUMBER |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `ICN` | ICN_ID | INDUSTRIAL CONTROL NUMBER |
| `ICN_ID` | ICN_ID | INDUSTRIAL CONTROL NUMBER |
| `JNLU_ID` | JNLU_ID | JOB ORDER NUMBER LOCAL USE IDENTIFIER |
| `KEYOP_ID` | KEYOP_ID | KEY OPERATION IDENTIFIER |
| `LASTMOD_USER_SA_ID` | LASTMOD_USER_SA_ID | LAST MODIFIED USER SYSTEM ASSIGNED ID |
| `MODIFIED_DATE_TZ` | MODIFIED_DATE_TZ | MODIFIED DATE WITH TIMEZONE |
| `SHOP_CD` | SHOP_CD | SHOP NUMBER CODE |
| `Shop Code` | SHOP_CD | SHOP NUMBER CODE |
| `TS_TSD_CD` | TS_TSD_CD | TRADE SKILL AND TRADE SKILL DESIGNATOR CODE |
| `bea_besa_jnlu_xref` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |

## `COST_Direct_Line_Item_Ref.qvd`  (10 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%JON_KEY` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, WKCCD, COWKE, JOSER | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, WKCCD: WORK_CATEGORY CODE, COWKE: COAR WORK EFFORT IDENTIFIER, JO |
| `CARGE_CODE` | COCHG | COAR CHARGE CODE |
| `COAR` | WKCCD, COWKE |  |
| `COAR Title` | COTTL | COAR TITLE |
| `EST_DATE` | COESD | COAR ESTABLISH DATE |
| `HULL` | SPTYP, SPSRL |  |
| `HULL_NBR` | SPSRL | SHIP HULL SERIAL NUMBER |
| `HULL_TYPE` | SPTYP | SHIP TYPE |
| `JON_TITLE` | JOTTL | JOB ORDER TITLE |
| `ROLL_OVER_IND` | COROI | COST ROLLOVER INDICATOR |

## `COST_FA05.qvd`  (15 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%FA05_MAT_Key` | ACTIVITY_SA_ID, AVNBR | ACTIVITY SYSTEM ASSIGNED ID |
| `%FO05_FA05_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, AVNBR | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER |
| `Availability Actual Compl Date` | AVACD | AVAILABILITY ACTUAL COMPLETION DATE |
| `Availability Actual Start Date` | AVASD | AVAILABILITY ACTUAL START DATE |
| `Availability Length in Months` | AVLNG | AVAILABILITY LENGTH IN MONTHS |
| `Availability Number` | AVNBR | AVAILABILITY NUMBER |
| `Availability Schedule Compl Date` | AVSCD | AVAILABILITY SCHEDULED COMPL DATE |
| `Availability Schedule Start Date` | AVSSD | AVAILABILITY SCHEDULED START DATE |
| `Availability WOJO Code` | AVWJO | AVAILABILITY WOJO CODE |
| `FA_05 Activity ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `Ship Hull Serial Number` | SPSRL | SHIP HULL SERIAL NUMBER |
| `Ship Type` | SPTYP | SHIP TYPE |
| `Shipyard Planned Compl Date` | AVPCD | SHIPYARD PLANNED COMPLETION DATE |
| `Shipyard Planned Start Date` | AVPSD | SHIPYARD PLANNED START DATE |
| `Work Category Group` | R1WKCCD | WORK CATEGORY GROUP |

## `COST_FE05.qvd`  (14 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%ICNKOP_KEY` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, WKCCD, COWKE, JOSER. KOPCD,  | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, WKCCD: WORK-CATEGORY CODE, COWKE: COAR WORK EFFORT IDENTIFIER, JO |
| `%JON_KEY` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, WKCCD, COWKE, JOSER | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, WKCCD: WORK-CATEGORY CODE, COWKE: COAR WORK EFFORT IDENTIFIER, JO |
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `COAR` | WKCCD, COWKE | WORK-CATEGORY CODE, COAR WORK EFFORT IDENTIFIER |
| `COWKE` | COWKE | COAR WORK EFFORT IDENTIFIER |
| `FISCAL_YEAR` | FY, FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `ICN_KOP` | WKCCD, COWKE, JOSER, KOPCD, KOWKT | WORK-CATEGORY CODE, COAR WORK EFFORT IDENTIFIER, JOB ORDER SERIALIZATION, KEYOP PHASE CODE, KEYOP WORK TYPE |
| `JON` | WKCCD, COWKE, JOSER | WORK-CATEGORY CODE, COAR WORK EFFORT IDENTIFIER, JOB ORDER SERIALIZATION |
| `JOSER` | JOSER | JOB ORDER SERIALIZATION |
| `KOPCD` | KOPCD | KEYOP PHASE CODE |
| `KOTTL` | KOTTL | KEYOP TITLE |
| `KOWKT` | KOWKT | KEYOP WORK TYPE |
| `WKCCD` | WKCCD | WORK-CATEGORY CODE |

## `COST_FE75.qvd`  (51 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Effcd_Clcde_Joser4_Kopcd_Kowkt_Key` | EFFCD, CLCDE, JOSER4, KOPCD, KOWKT, ACTIVITY_SA_ID, FISCAL_Y | EFFCD: EXPENSE FUNCTION CODE, CLCDE: COST CLASS CODE, JOSER4: JOB ORDER SERIALIZATION LAST 4, KOPCD: KEYOP PHASE CODE, KOWKT: KEYOP WORK TYPE, ACTIVIT |
| `%FJ90_FE75_Key, //Same key to FJ90 and FJ7` | EFFCD, CLCDE, JOSER4, ACTIVITY_SA_ID, FISCAL_YEAR_ID | EFFCD: EXPENSE FUNCTION CODE, CLCDE: COST CLASS CODE, JOSER4: JOB ORDER SERIALIZATION LAST 4, ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR |
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `KO Allowance Revisions` | KOARV | KO ALLOWANCE REVISIONS |
| `Key Event Number` | EVNBR |  |
| `Key Shop Number` | SHNBRK | KEY SHOP NUMBER |
| `KeyOp Actual Closed Date` | KOCLD | KEYOP ACTUAL CLOSED DATE |
| `KeyOp Actual Completion Date` | KOACD | KEYOP ACTUAL COMPLETION DATE |
| `KeyOp Actual Start Date` | KOASD | KEYOP ACTUAL START DATE |
| `KeyOp Allowance Revision Date` | KOARD | KEYOP ALLOWANCE REVISION DATE |
| `KeyOp Area Code PC Type 3` | KOARC | KEYOP AREA CODE PC TYPE 3 |
| `KeyOp Automatic Closure Code` | KOACC | KEYOP AUTOMATIC CLOSURE CODE |
| `KeyOp Closed to Labor Date` | KODCL | KEY OPERATION CLOSED TO LABOR DATE |
| `KeyOp Closure Code` | KOCLC | KEYOP CLOSURE CODE |
| `KeyOp Critical Code` | KOCCD | KEYOP CRITICAL CODE |
| `KeyOp DMI Amount` | KEDMI | KEYOP DMI AMOUNT |
| `KeyOp Establishment Date` | KOESD | KEYOP ESTABLISHMENT DATE |
| `KeyOp Estimate Revision` | KOERV | KO ESTIMATE REVISION |
| `KeyOp Estimate Revision Date` | KOERD | KEYOP ESTIMATE REVISION DATE |
| `KeyOp Final Manhour Allowance IND` | KOFMA | KEYOP FINAL MANHOUR ALLOWANCE IND |
| `KeyOp Funds Control Code` | KOFCC | KEYOP FUNDS CONTROL CODE |
| `KeyOp Jeopardy Control Indicator` | KOJCI | KEYOP JEOPARDY CONTROL INDICATOR |
| `KeyOp Material Need (Percent)` | KOMPN | KEYOP - MATERIAL NEEDED ( PERCENT ) |
| `KeyOp Milestone Number` | KOMSN | KEYOP MILESTONE NUMBER |
| `KeyOp Outstand Contract SRVC Commit` | KECCO | KEYOP OUTSTAND CONTRACT SRVC COMMIT |
| `KeyOp Outstand Contract SRVC Obl Amt` | KEOCO | KEYOP OUTSTAND CONTRACT SRVC OBL AMT |
| `KeyOp Outstand Material Oblig Amount` | KEOMO | KEYOP OUTSTAND MATERIAL OBLIG AMOUNT |
| `KeyOp Outstand Other Cost Commitment` | KECOO | KEYOP OUTSTAND OTHER COST COMMITMENT |
| `KeyOp Outstand Other Cost Oblig Amt` | KEOOO | KEYOP OUTSTAND OTHER COST OBLIG AMT |
| `KeyOp Outstanding Matl Commit Amt` | KECMO | KEYOP OUTSTANDING MATL COMMIT AMT |
| `KeyOp Phase Code` | KOPCD | KEYOP PHASE CODE |
| `KeyOp Porgress Compl Percent` | KOPCP | KEYOP PROGRESS COMPL PERCENT |
| `KeyOp Priority Indicator` | KOPRI | KEYOP PRIORITY INDICATOR |
| `KeyOp Radcon Exposure Code` | KOREC | KEYOP RADCON EXPOSURE CODE |
| `KeyOp Rescheduling Reason Code` | KORSR | KEYOP RESCHEDULING REASON CODE |
| `KeyOp Revised Schedule Complete Date` | KORCD | KEYOP REVISED SCHEDULE COMPLETE DATE |
| `KeyOp Revised Schedule Start Date` | KORSD | KEYOP REVISED SCHEDULED START DATE |
| `KeyOp Revsn to Compl Date Number` | KONRC | KEYOP REVSN TO COMPL DATE NUMBER |
| `KeyOp Revsn to Start Date Number` | KONRS | KEYOP REVSN TO START DATE NUMBER |
| `KeyOp Schedule Start Date` | KOSSD | KEYOP SCHEDULED START DATE |
| `KeyOp Scheduled Completion Date` | KOSCD | KEYOP SCHEDULED COMPLETION DATE |
| `KeyOp Scheduled Issue Date` | KOSID | KEYOP SCHEDULED ISSUE DATE |
| `KeyOp System Code` | KOSYC | KEYOP SYSTEM CODE |
| `KeyOp Title` | KOTTL | KEYOP TITLE |
| `KeyOp Work Indicator Code` | KOWIC | KO WORK INDICATOR CODE |
| `KeyOp Work Measurement Code` | KOWMC | KEYOP WORK MEASUREMENT CODE |
| `KeyOp Work Status Code` | KOWSC | KEYOP WORK STATUS CODE |
| `KeyOp Work Type` | KOWKT | KEYOP WORK TYPE |
| `Reschedule Supervisor Code` | KORSC | RESCHEDULE SUPERVISOR CODE |
| `Trade Skill Designator - Key` | WCNBRK | TRADE SKILL DESIGNATOR - KEY |

## `COST_FE77.qvd`  (20 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Effcd_Clcde_Joser4_Kopcd_Kowkt_Key` | EFFCD, CLCDE, JOSER4, KOPCD, KOWKT, ACTIVITY_SA_ID, FISCAL_Y | EFFCD: EXPENSE FUNCTION CODE, CLCDE: COST CLASS CODE, JOSER4: JOB ORDER SERIALIZATION LAST 4, KOPCD: KEYOP PHASE CODE, KOWKT: KEYOP WORK TYPE, ACTIVIT |
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `Cost Class Code` | CLCDE | COST CLASS CODE |
| `Expense Function Code` | EFFCD | EXPENSE FUNCTION CODE |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `JO/KO/SH MLC/FN OT OBL/EXP AMT (ITD)` | KOS_FN_OT_ITD_AM | JO/KO/SH MLC/FN OT OBL/EXP AMT (ITD) |
| `JO/KO/SH MLC/FN OT OBL/EXP AMT (MTD)` | KOS_FN_OT_MTD_AM | JO/KO/SH MLC/FN OT OBL/EXP AMT (MTD) |
| `JO/KO/SH MLC/FN OT OBL/EXP AMT(WTD)` | KOS_FN_OT_WTD_AM | JO/KO/SH MLC/FN OT OBL/EXP AMT (WTD) |
| `JO/KO/SH MLC/FN OT OBL/EXP HR (ITD)` | KOS_FN_OT_ITD_QY | JO/KO/SH MLC/FN OT OBL/EXP HR (ITD) |
| `JO/KO/SH MLC/FN OT OBL/EXP HR (MTD)` | KOS_FN_OT_MTD_QY | JO/KO/SH MLC/FN OT OBL/EXP HR (MTD) |
| `JO/KO/SH MLC/FN OT OBL/EXP HR (WTD)` | KOS_FN_OT_WTD_QY | JO/KO/SH MLC/FN OT OBL/EXP HR (WTD) |
| `JO/KO/SH MLC/FN REG OBL/EXP AMT (ITD)` | KOS_FN_REG_ITD_AM | JO/KO/SH MLC/FN REG OBL/EXP AMT(ITD) |
| `JO/KO/SH MLC/FN REG OBL/EXP AMT (MTD)` | KOS_FN_REG_MTD_AM | JO/KO/SH MLC/FN REG OBL/EXP AMT(MTD) |
| `JO/KO/SH MLC/FN REG OBL/EXP AMT (WTD)` | KOS_FN_REG_WTD_AM | JO/KO/SH MLC/FN REG OBL/EXP AMT(WTD) |
| `JO/KO/SH MLC/FN REG OBL/EXP HR (ITD)` | KOS_FN_REG_ITD_QY | JO/KO/SH MLC/FN REG OBL/EXP HR (ITD) |
| `JO/KO/SH MLC/FN REG OBL/EXP HR (MTD)` | KOS_FN_REG_MTD_QY | JO/KO/SH MLC/FN REG OBL/EXP HR (MTD) |
| `JO/KO/SH MLC/FN REG OBL/EXP HR (WTD)` | KOS_FN_REG_WTD_QY | JO/KO/SH MLC/FN REG OBL/EXP HR (WTD) |
| `Job Order Serialization Last 4` | JOSER4 | JOB ORDER SERIALIZATION LAST 4 |
| `KeyOp Phase Code` | KOPCD | KEYOP PHASE CODE |
| `KeyOp Work Type` | KOWKT | KEYOP WORK TYPE |

## `COST_FF05.qvd`  (6 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Fdfdn_Key,//Key to FF10 and FF40 table` | FDFDN, ACTIVITY_SA_ID, FISCAL_YEAR_ID | FDFDN: FUNDING DOCUMENT NUMBER, ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER |
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `Funding Document Expiration Date` | FDEXD | FUNDING DOCUMENT EXPIRATION DATE |
| `Funding Document Number` | FDFDN | FUNDING DOCUMENT NUMBER |
| `RON_ID` | RON_ID | FULL REIMBURSABLE ORDER NUMBER (RON) ID |

## `COST_FH05.qvd`  (13 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%FH05_MAT_Key` | ACTIVITY_SA_ID, SPTYP, SPSRL | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, SPTYP: SHIP TYPE, SPSRL: SHIP HULL SERIAL NUMBER |
| `%FO05_FH05_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, SPTYP, SPSRL | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, SPTYP: SHIP TYPE, SPSRL: SHIP HULL SERIAL NUMBER |
| `Default Cost Account Code` | JOCACD | DEFAULT COST ACCOUNT CODE |
| `FH05 Activity ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `SHIP_RIC_ID` | SHIP_RIC_ID |  |
| `Ship Abbreviated Name` | SPABR | SHIP ABBREVIATED NAME |
| `Ship Class Code` | SPCLS | SHIP CLASS CODE |
| `Ship Fleet/Subtycom Code` | SPFLT | SHIP FLEET/SUBTYCOM CODE |
| `Ship Full Name` | SPNME | SHIP FULL NAME |
| `Ship Hull Serial Number` | SPSRL | SHIP HULL SERIAL NUMBER |
| `Ship Type` | SPTYP | SHIP TYPE |
| `Ship Type Commander` | SPTYC | SHIP TYPE COMMANDER |
| `Unit Identification Code` | AAUIC | UNIT IDENTIFICATION CODE |

## `COST_FJ13.qvd`  (8 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `COAR` | WKCCDF, COWKEF | WKCCDF: WORK CATEGORY CODE -FCN, COWKEF: COAR WORK EFFORT FCN IDENTIFIER |
| `FCN` | WKCCDF, COWKEF, JOSERF | WKCCDF: WORK CATEGORY CODE -FCN, COWKEF: COAR WORK EFFORT FCN IDENTIFIER, JOSERFJOB ORDER FCN SERIALIZATION |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `ICN` | WKCCDI, COWKEI, JOSERI | WKCCDI: WORK CATEGORY CODE -ICN, COWKEI: COAR WORK EFFORT ICN IDENTIFIER, JOSERI: JOB ORDER ICN SERIALIZATION |
| `KEYOP` | KOPCD, KOWKT | KOPCD: KEYOP PHASE CODE, KOWKT: KEYOP WORK TYPE |
| `KO FCN Labor Percentage` | KOLBP | KEYOP FCN LABOR PERCENT |
| `KO FCN Material Percentage` | KOMLP | KO FCN MATERIAL PERCENT |

## `COST_FJ40.qvd`  (29 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%FO05_FJ40_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, WKCCD, COWKE | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, WKCCD: WORK-CATEGORY CODE, COWKE: COAR WORK EFFORT IDENTIFIER |
| `%Shnbr_Key, //Key to FS1` | SHNBR, ACTIVITY_SA_ID, FISCAL_YEAR_ID | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER |
| `%Wkccd_Cowke_Joser_Shnbr_Key, //Same Key needs to be put in FJ41 and FJ4` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, WKCCD, COWKE, JOSER, SHNBR | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, WKCCD: WORK-CATEGORY CODE, COWKE: COAR WORK EFFORT IDENTIFIER, JO |
| `` |  |  |
| `JO Holiday Accel Labor Graded Amount` | JCHAG | JO HOLIDAY ACCEL LABOR GRADED AMOUNT |
| `JO Holiday Accel Labor Ungraded Amount` | JCHAU | JO HOLIDAY ACCEL LABOR UNGRADED AMT |
| `JO Holiday Labor Graded Hours` | JCHHG | JO HOLIDAY LABOR GRADED HOURS |
| `JO Holiday Labor Ungraded Hours` | JCHHU | JO HOLIDAY LABOR UNGRADED HOURS |
| `JO Material Receipts - A/P` | JCDMA | JO MATERIAL RECEIPTS - A/P |
| `JO Overtime Accel Lbr Grd Amount` | JCOAG | JO OVERTIME ACCEL LBR GRD AMT |
| `JO Overtime Accel Lbr Ungrd Amount` | JCOAU | JO OVERTIME ACCEL LBR UNGRD AMOUNT |
| `JO Overtime Labor Graded Hours` | JCOHG | CIV OVERTIME LABOR GRADED HOURS |
| `JO Overtime Labor Ungraded Hours` | JCOHU | CIV OVERTIME LABOR UNGRADED HOURS |
| `JO Straight Time Accel Lbr Grd Amt` | JCSAG | JO STRAIGHT TIME ACCEL LBR GRD AMT |
| `JO Straight Time Accel Lbr Ungrd Amt` | JCSAU | JO STRAIGHT TIME ACCEL LBR UNGRD AMT |
| `JO Straight Time Lbr Graded Hours` | JCSHG | JO STRAIGHT TIME LABOR GRADED HOURS |
| `JO Straight Time Lbr Ungraded Hours` | JCSHU | JO STRAIGHT TIME LABOR UNGRADED HRS |
| `Job Order Estimated Manhours` | JALMH | JOB ORDER ESTIMATED MANHOURS |
| `MCL_OT_QY` | JOS_FN_OTX_ITD_QY | JO/SH MLC/FN OT OBL/EXP HRS (ITD) |
| `MLC_OT_AM` | JOS_FN_OTX_ITD_AM | JO/SH MLC/FN OT OBL/EXP AMT (ITD) |
| `MLC_REG_AM` | JOS_FN_REGX_ITD_AM | JO/SH MLC/FN REG OBL/EXP AMT (ITD) |
| `MLC_REG_Q` | JOS_FN_REGX_ITD_QY | JO/SH MLC/FN REG OBL/EXP HRS (ITD) |
| `Stars Cont Services Exp Amount` | STCSA | STARS CONT SERVICES EXP AMOUNT |
| `Stars Material Expended Amount` | STMAT | STARS MATERIAL EXPENDED AMOUNT |
| `Stars Other Cost Exp Amount` | STOTH | STARS OTHER COST EXP AMOUNT |
| `Stars Overtime Hours` | STOHR | STARS OVERTIME HOURS |
| `Stars Overtime Labor Amount` | STOAG | STARS OVERTIME LABOR AMOUNT |
| `Stars Regular Hours` | STRHR | STARS REGULAR HOURS |
| `Stars Regular Time Amount` | STSAG | STARS REGULAR TIME AMOUNT |

## `COST_FJ77.qvd`  (5 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%FM40_FJ77_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, EFFCD | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, EFFCD: EXPENSE FUNCTION CODE |
| `MCL_OT_QY` | JOS_FN_OTX_YTD_QY | JO/SH MLC/FN OT OBL/EXP HRS (YTD) |
| `MLC_OT_AM` | JOS_FN_OTX_YTD_AM | JO/SH MLC/FN OT OBL/EXP AMT (YTD) |
| `MLC_REG_AM` | JOS_FN_REGX_YTD_AM | JO/SH MLC/FN REG OBL/EXP AMT (YTD) |
| `MLC_REG_QY` | JOS_FN_REGX_YTD_QY | JO/SH MLC/FN REG OBL/EXP HRS (YTD) |

## `COST_FJ90.qvd`  (1 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%JON_KEY` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, EFFCD, CLCDE, JOSER4 | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, EFFCD: EXPENSE FUNCTION CODE, CLCDE: COST CLASS CODE, JOSER4: JOB |

## `COST_FM25.qvd`  (4 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Ctcod_Key,//Key to FS10 Tabl` | CTCOD, ACTIVITY_SA_ID | CTCOD: COST-CENTER CODE, ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID |
| `Cost Center Name` | CTNME | COST CENTER NAME |
| `Cost Center Type` | CTTYP | COST CENTER TYPE |
| `Department Number` | DENBR | DEPARTMENT NUMBER |

## `COST_FM40.qvd`  (6 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `Expense Function Code` | EFFCD | EXPENSE FUNCTION CODE |
| `Expense Function Name` | EFNME | EXPENSE FUNCTION NAME |
| `FM40 Activity ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `FM40 Fiscal Year` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `Funds Administrator Code` | FACDE | FUNDS ADMINISTRATOR CODE |

## `COST_FO05.qvd`  (24 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%FO05_FA05_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, AVNBR | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, AVNBR: AVAILABILITY NUMBER |
| `%FO05_FH05_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, SPTYP, SPSRL | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, SPTYP: SHIP TYPE, SPSRL: SHIP HULL SERIAL NUMBER |
| `%FO05_FM40_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, BEA_CD, BESA_ID | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, BEA_CD: BUDGET EXECUTION ACTIVITY CODE, BESA_ID: BUDGET EXECUTION |
| `%Wkccd_Cowke_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, WKCCD, COWKE | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, WKCCD: WORK-CATEGORY CODE, COWKE: COAR WORK EFFORT IDENTIFIER |
| `COAR Charge Code` | COCHG | COAR CHARGE CODE |
| `COAR Establish Date` | COESD | COAR ESTABLISH DATE |
| `COAR Labor Funds Authorized Amount` | COLTFA | COAR LABOR FUNDS AUTHORIZED AMOUNT |
| `COAR Material Funds Authorized Amt` | COMTFA | COAR MATERIAL FUNDS AUTHORIZED AMNT |
| `COAR Nuclear Code` | CONUC | COAR NUCLEAR CODE |
| `COAR Outstanding Commitment Matl Amt` | CCCMO | COAR OUTSTANDING COMMITMENT MATL AMT |
| `COAR Outstd Contractual Srvc Obl Amt` | CCOCO | COAR OUTSTD CONTRACTUAL SRVC OBL AMT |
| `COAR Outstd Ctrl Srvc Commit Amt` | CCCCO | COAR OUTSTD CTRL SRVC COMMIT AMT |
| `COAR Outstd Matl Obligations Amt` | CCOMO | COAR OUTSTD MATL OBLIGATIONS AMT |
| `COAR Outstd Other Cost Commit Amt` | CCCOO | COAR OUTSTD OTHER COST COMMIT AMT |
| `COAR Outstd Other Cost Obl Amt` | CCOOO | COAR OUTSTD OTHER COST OBL AMT |
| `COAR Scheduled Completion Date` | COSCD | COAR SCHEDULED COMPLETION DATE |
| `COAR Scheduled Start Date` | COSSD | COAR SCHEDULED START DATE |
| `COAR Total Funds Authorized Amount` | COTFA | COAR TOTAL FUNDS AUTHORIZED AMOUNT |
| `COAR Work Effort Identifier` | COWKE | COAR WORK EFFORT IDENTIFIER |
| `COAR_TITLE` | COTTL | COAR TITLE |
| `Cost Rollover Indicator` | COROI | COST ROLLOVER INDICATOR |
| `Funding Source Indicator` | FDSRC | FUNDING SOURCE INDICATOR |
| `Funds Administrator Code` | FACDE | FUNDS ADMINISTRATOR CODE |
| `Work Category Code` | WKCCD | WORK-CATEGORY CODE |

## `COST_FO05_FM40.qvd`  (35 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%BBJS_FO05_FM40_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, BEA_CD, BESA_ID | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, BEA_CD: BUDGET EXECUTION ACTIVITY CODE, BESA_ID: BUDGET EXECUTION |
| `%FM40_FJ77_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, EFFCD | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, EFFCD: EXPENSE FUNCTION CODE |
| `%FO05_FJ40_Key` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, WKCCD, COWKE | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, WKCCD: WORK-CATEGORY CODE, COWKE: COAR WORK EFFORT IDENTIFIER |
| `BEA_CD` | BEA_CD | BUDGET EXECUTION ACTIVITY (BEA) CODE |
| `BEA_CD` | BEA_CD | BUDGET EXECUTION ACTIVITY CODE |
| `BESA_ID` | BESA_ID | BUDGET EXECUTION SUB-ACTIVITY (BESA) ID |
| `BESA_ID` | BESA_ID | BUDGET EXECUTION SUB-ACTIVITY (BESA) ID |
| `COAR_ID` |  |  |
| `COAR_ID` | WKCCD, COWKE | WORK-CATEGORY CODE, COAR WORK EFFORT IDENTIFIER |
| `CR_START_DT` | R1CRDTE | CREATION DATE |
| `CR_START_DT` | COSSD | COAR SCHEDULED START DATE |
| `EXP_FUNC_CD` | EFFCD | EXPENSE FUNCTION CODE |
| `EXP_FUNC_CD` |  |  |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `LAST_COMPL_DT` | R1LDATE | DATE OF LAST TRANSACTION |
| `LAST_COMPL_DT` | COSCD | COAR SCHEDULED COMPLETION DATE |
| `LBR_FUND_STAT_CD` | FSTATL | FUNDING STATUS CODE - LABOR |
| `LBR_FUND_STAT_CD` | FSTATL | FUNDING STATUS CODE - LABOR |
| `LBR_TFA_AM` | DOLTFA | TOTAL LABOR FUNDS AUTHORIZED AM |
| `LBR_TFA_AM` | COLTFA | COAR LABOR FUNDS AUTHORIZED AMOUNT |
| `MATL_FUND_STAT_CD` | FSTATM | FUNDING STATUS CODE - MATERIAL |
| `MATL_FUND_STAT_CD` | FSTATM | FUNDING STATUS CODE - MATERIAL |
| `MATL_TFA_AM` | DOMTFA | TOTAL MATERIAL AUTHORIZED AMT |
| `MATL_TFA_AM` | COMTFA | COAR MATERIAL FUNDS AUTHORIZED AMNT |
| `OB_REIMB_CD` | FDSRC | FUNDING SOURCE INDICATOR |
| `OB_REIMB_CD` | FDSRC | FUNDING SOURCE INDICATOR |
| `Ship Type` |  |  |
| `Ship Type` | SPTYP | SHIP TYPE |
| `TFA_AM` | DOTFA | DEPT TOTAL FUNDS AUTHORIZED AMOUNT |
| `TFA_AM` | COTFA | COAR TOTAL FUNDS AUTHORIZED AMOUNT |
| `TTL_NME` | EFNME | EXPENSE FUNCTION NAME |
| `TTL_NME` | COTTL | COAR TITLE |
| `WCI_FC_SIC_BEA_ID` | WCI_FC_SIC_BEA_ID | WCI FUND CODE SIC BEA SYS ASSIGNED ID |
| `WCI_FC_SIC_BEA_ID` | WCI_FC_SIC_BEA_ID | WCI FUND CODE SIC BEA SYS ASSIGNED ID |

## `COST_FS10.qvd`  (32 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Ctcod_Key, //Key to FM25 tabl` | CTCOD, ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `%Shnbr_Key` | SHNBR, ACTIVITY_SA_ID,FISCAL_YEAR_ID | SHNBR: SHOP-NUMBER IDENTIFIER, ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER |
| `Acceleration Table Identifier` | ARIND | ACCELERATION-TABLE IDENTIFIER |
| `Active/Inactive Indicator Code` | R2AIIND | ACTIVE/INACTIVE INDICATOR CODE |
| `Cost Center Code` | CTCOD | COST-CENTER CODE |
| `Expense Job Order Number` | JONBRE | EXPENSE JOB ORDER NUMBER |
| `Group Number Identifier` | GRNBR | GROUP-NUMBER IDENTIFIER |
| `Inactive Effective Date` | R2AIDTE | INACTIVE EFFECTIVE DATE |
| `New Rates Effective Date` | R2REDTE | NEW RATES EFFECTIVE DATE |
| `Overhead Job Order TS/TSD Default` | DFLT_TS_TSD_CD | OVERHEAD JOB ORDER TS/TSD DEFAULT |
| `Shop - Applied G&A Overhead New Rate` | SROHGN | SHOP - APPLIED G&A OVERHEAD NEW RATE |
| `Shop - Applied G&A Overhead Rate` | SROHG | SHOP - APPLIED G&A OVERHEAD RATE |
| `Shop - Stabilized Labor Rate` | SRSLR | SHOP - STABILIZED LABOR RATE |
| `Shop - Stabilized Material Rate` | SRSMR | SHOP - STABILIZED MATERIAL RATE |
| `Shop Allowance Load Rate` | SRALL | SHOP ALLOWANCE LOAD RATE |
| `Shop Applied PROD Overhead New Rate` | SROHPN | SHOP APPLIED PROD OVERHEAD NEW RATE |
| `Shop Applied PROD Overhead Rate` | SROHP | SHOP APPLIED PROD OVERHEAD RATE |
| `Shop Average Labor New Rate` | SRAVLN | SHOP AVERAGE LABOR NEW RATE |
| `Shop Average Labor Rate` | SRAVL | SHOP AVERAGE LABOR RATE |
| `Shop Estimate Load Rate` | SRESL | SHOP ESTIMATE LOAD RATE |
| `Shop Name` | SHNME | SHOP NAME |
| `Shop Perf Factor Average AMT` | SHPFA | SHOP PERF FACTOR AVERAGE AMT |
| `Shop Perf Factor Eng Standards AMT` | SHPFE | SHOP PERF FACTOR ENG STANDARDS AMT |
| `Shop Perf Factor Est Standars AMT` | SHPES | SHOP PERF FACTOR EST STANDARDS AMT |
| `Shop Perf Factor Non-Standards AMT` | SHPNS | SHOP PERF FACTOR NON-STANDARDS AMT |
| `Shop Perf Factor Uniform STD AMT` | SHPUS | SHOP PERF FACTOR UNIFORM STD AMT |
| `Shop Special G & A OH New Rate-1` | SROH1N | SHOP SPECIAL G & A OH NEW RATE-1 |
| `Shop Special G & A OH New Rate-2` | SROH2N | SHOP SPECIAL G & A OH NEW RATE-2 |
| `Shop Special G & A Overhead Rate-1` | SROH1 | SHOP SPECIAL G & A OVERHEAD RATE-1 |
| `Shop Special G & A Overhead Rate-2` | SROH2 | SHOP SPECIAL G & A OVERHEAD RATE-2 |
| `Shop Supervisor Code` | SHSPV | SHOP SUPERVISOR CODE |
| `Shop Travel Indicator` | SHTRI | SHOP TRAVEL INDICATOR |

## `COST_Overhead_JON_Ref.qvd`  (20 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%ICNKOP_KEY` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, EFFCD, CLCDE, JOSER4, KOPCD, | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, EFFCD: EXPENSE FUNCTION CODE, CLCDE: COST CLASS CODE, JOSER4: JOB |
| `%JON_KEY` | ACTIVITY_SA_ID, FISCAL_YEAR_ID, EFFCD, CLCDE, JOSER4 | ACTIVITY_SA_ID: ACTIVITY SYSTEM ASSIGNED ID, FISCAL_YEAR_ID: FISCAL YEAR IDENTIFIER, EFFCD: EXPENSE FUNCTION CODE, CLCDE: COST CLASS CODE, JOSER4: JOB |
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `CLCDE` | CLCDE | COST CLASS CODE |
| `COAR` | EFFCD, CLCDE | EXPENSE FUNCTION CODE |
| `EFFCD` | EFFCD | EXPENSE FUNCTION CODE |
| `FISCAL_YEAR` | FY, FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `ICN_KOP` | EFFCD, CLCDE, JOSER4, KOPCD, KOWKT | EFFCD: EXPENSE FUNCTION CODE, CLCDE: COST CLASS CODE, JOSER4: JOB ORDER SERIALIZATION LAST 4, KOPCD: KEYOP PHASE CODE, KOWKT: KEYOP WORK TYPE |
| `JON` | EFFCD, CLCDE, JOSER4 | EFFCD: EXPENSE FUNCTION CODE, CLCDE: COST CLASS CODE, JOSER4: JOB ORDER SERIALIZATION LAST 4 |
| `JON_TYPE` | EFFCD | EXPENSE FUNCTION CODE |
| `JO_Title` | JOTTL | JOB ORDER TITLE |
| `KOP` | KOPCD, KOWKT |  |
| `KOPCD` | KOPCD | KEYOP PHASE CODE |
| `KOWKT` | KOWKT | KEYOP WORK TYPE |
| `KO_Title` | KOTTL | KEYOP TITLE |
| `LAST4` | JOSER4 | JOB ORDER SERIALIZATION LAST 4 |
| `Shop_Key` | SHNBRK | KEY SHOP NUMBER |
| `Shop_Lead` | SHNBRL | LEAD SHOP NUMBER |
| `TS/TSD_Key` | WCNBRK | TRADE SKILL DESIGNATOR - KEY |
| `TS/TSD_Lead` | WCNBRL | TRADE SKILL DESIGNATOR - LEAD |

## `COST_TRVL_SV_DOC.qvd`  (15 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `ACTIVITY_SA_ID` | ACTIVITY_SA_ID | ACTIVITY SYSTEM ASSIGNED ID |
| `COMMITMENT_AM` | COMMITMENT_AM | COMMITMENT AMOUNT |
| `EXPENSE_AM` | EXPENSE_AM | EXPENSE AMOUNT |
| `FCN_ID` | FCN_ID | FINANCIAL CONTROL JOB ORDER NUMBER |
| `FISCAL_YEAR_ID` | FISCAL_YEAR_ID | FISCAL YEAR IDENTIFIER |
| `KEYOP_ID` | KEYOP_ID | KEY OPERATION IDENTIFIER |
| `LIQUIDATION_AM` | LIQUIDATION_AM | LIQUIDATION AMOUNT |
| `LOA` | LOA |  |
| `OBLIGATION_AM` | OBLIGATION_AM | OBLIGATION AMOUNT |
| `PROCEED_DT` | PROCEED_DT | PROCEED ON OR ABOUT DATE |
| `SHOP_CD` | SHOP_CD | SHOP NUMBER CODE |
| `SOCC_ID` | SOCC_ID | SUB-OBJECT CLASS CODE IDENTIFIER |
| `STD_DOC_ID` | STD_DOC_ID | STANDARD DOCUMENT NUMBER (SDN) ID |
| `TRAVELER_NAME_TX` | TRAVELER_NAME_TX | TRAVELER NAME |
| `TRVL_SV_DOC` | TRVL_SV_DOC |  |

---

# MAT schema

## `MAT_Materials.qvd`  (232 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%Cu_Phase_MAT_Key` | ACTIVITY_SA_ID, M05_JO_KO |  |
| `%FA05_MAT_Key` | ACTIVITY_SA_ID, M02_AVAIL_NR |  |
| `%FH05_MAT_Key` | ACTIVITY_SA_ID, M02_HULL_NR |  |
| `%M02_M03_Key` | ACTIVITY_SA_ID, M02_AVAIL_NR |  |
| `%M02_M03_Key` | ACTIVITY_SA_ID, M03_M02_AVAIL_NR |  |
| `%M03_M04_Key` | ACTIVITY_SA_ID, M03_EXPENSE_ACCOUNT |  |
| `%M03_M04_Key` | ACTIVITY_SA_ID, M04_M03_EXPENSE_ACCOUNT |  |
| `%M04_M05_Key` | ACTIVITY_SA_ID, M04_JO |  |
| `%M04_M05_Key` | ACTIVITY_SA_ID, M05_M04_JO |  |
| `%M05_M10_Key` | ACTIVITY_SA_ID, M05_JO_KO |  |
| `%M05_M10_Key` | ACTIVITY_SA_ID, M10_M05_JO_KO |  |
| `%M10_M102_Key` | ACTIVITY_SA_ID, M10_DOC_CUT_NR |  |
| `%M10_M102_Key` | ACTIVITY_SA_ID, M102_M101_DOC_CUT_NR |  |
| `%M10_M11_Key` | ACTIVITY_SA_ID, M10_DOC_CUT_NR |  |
| `%M10_M11_Key` | ACTIVITY_SA_ID, M11_M10_DOC_CUT_NR |  |
| `%M10_M12_Key` | ACTIVITY_SA_ID, M10_DOC_CUT_NR |  |
| `%M10_M12_Key` | ACTIVITY_SA_ID, M12_M10_DOC_CUT_NR |  |
| `%M10_M14_Key` | ACTIVITY_SA_ID, M10_DOC_CUT_NR |  |
| `%M10_M14_Key` | ACTIVITY_SA_ID, M14_M10_DOC_CUT_NR |  |
| `%M10_M23_Key` | ACTIVITY_SA_ID, M10_M23_PIIN_CALL_NR |  |
| `%M10_M23_Key` | ACTIVITY_SA_ID, M23_PIIN_CALL_NR |  |
| `%M10_M30_Key` | ACTIVITY_SA_ID, M10_M30_NIIN_SMIC |  |
| `%M10_M30_Key` | ACTIVITY_SA_ID, M30_NIIN_SMIC |  |
| `%M10_M32_Key` | ACTIVITY_SA_ID, M10_M30_NIIN_SMIC |  |
| `%M10_M32_Key` | ACTIVITY_SA_ID, M32_M230_NIIN_SMIC |  |
| `%M32_M230_Key` | ACTIVITY_SA_ID, M230_NIIN_SMIC |  |
| `%M35_M30_Key` | ACTIVITY_SA_ID, M30_NIIN_SMIC |  |
| `%M35_M30_Key` | ACTIVITY_SA_ID, M35_M30_NIIN_SMIC |  |
| `10th Prior Month Issue Count` | M32_10TH_PRIOR_ISS_CNT |  |
| `10th Prior Month Replen.Demand` | M32_10TH_PRIOR_REPLEN_DMD |  |
| `11th Prior Month Issue Count` | M32_11TH_PRIOR_ISS_CNT |  |
| `11th Prior Month Replen.Demand` | M32_11TH_PRIOR_REPLEN_DMD |  |
| `1st Prior Month Issue Count` | M32_1ST_PRIOR_ISS_CNT |  |
| `1st Prior Month Replen.Demand` | M32_1ST_PRIOR_REPLEN_DMD |  |
| `2nd Prior Month Issue Count` | M32_2ND_PRIOR_ISS_CNT |  |
| `2nd Prior Month Replen.Demand` | M32_2ND_PRIOR_REPLEN_DMD |  |
| `3rd Prior Month Issue Count` | M32_3RD_PRIOR_ISS_CNT |  |
| `3rd Prior Month Replen.Demand` | M32_3RD_PRIOR_REPLEN_DMD |  |
| `4th Prior Month Issue Count` | M32_4TH_PRIOR_ISS_CNT |  |
| `4th Prior Month Replen.Demand` | M32_4TH_PRIOR_REPLEN_DMD |  |
| `5th Prior Issue Month Count` | M32_5TH_PRIOR_ISS_CNT |  |
| `5th Prior Month Replen.Demand` | M32_5TH_PRIOR_REPLEN_DMD |  |
| `6th Prior Month Issue Count` | M32_6TH_PRIOR_ISS_CNT |  |
| `6th Prior Month Replen.Demand` | M32_6TH_PRIOR_REPLEN_DMD |  |
| `7th Prior Month Issue Count` | M32_7TH_PRIOR_ISS_CNT |  |
| `7th Prior Month Replen.Demand` | M32_7TH_PRIOR_REPLEN_DMD |  |
| `8th Prior Month Issue Count` | M32_8TH_PRIOR_ISS_CNT |  |
| `8th Prior Month Replen.Demand` | M32_8TH_PRIOR_REPLEN_DMD |  |
| `9th Prior Month Issue Count` | M32_9TH_PRIOR_ISS_CNT |  |
| `9th Prior Month Replen.Demand` | M32_9TH_PRIOR_REPLEN_DMD |  |
| `Acquisition Advice Code` | M32_ACQUISITION_ADVICE_CD |  |
| `Activity ID` | ACTIVITY_SA_ID |  |
| `Activity Name` | ACTIVITY_SA_ID |  |
| `Advice Code` | M10_ADVICE_CD |  |
| `Age Factor` | M32_AGE_FACTOR |  |
| `Availibility Number` | M02_AVAIL_NR |  |
| `Beginning On Hand Quantity` | M32_QTY_OH_BEGIN |  |
| `COAR` | M05_JO_KO |  |
| `Category Code` | M32_CATEGORY_CD |  |
| `Clean Grade` | M11_CLEAN_GRADE |  |
| `Closed to Labor Date` | M04_DATE_CLOSED_TO_LBR |  |
| `Cognizance Symbol Code` | M30_COG |  |
| `Commitment Code` | M10_COMIT_CD |  |
| `Commitment Code Name` | M10_COMIT_CD |  |
| `Commitment Job Order ID` | M11_COMMITMENT_JO_ID |  |
| `Committed Value` | M10_VALUE_COMIT |  |
| `Contract Award Date` | X_M23_DATE_CONTRACT | Date type column for M23_DATE_CONTRACT |
| `Contract Item Number` | M10_CONTR_ITEM_NR |  |
| `Conversion Factor` | M32_CONVERSION_FACTOR |  |
| `Credit Card Assigned to Buyer Date` | M10_ASSIGNED_TO_BUYER_DATE | The date the Purchase Card requisition was assigned to a buyer (Received in Purchase). |
| `Credit Card Buyer Code` | M10_PC_BUYER_CD |  |
| `Credit Card Foreign Currency  Value` | M10_FORGN_CURR_CC_PURCHASE_AM | Identifies the foreign currency purchase amount. |
| `Credit Card Purchase Date` | M10_CC_PURCHASE_DATE | Date of the Purchase Card procurement. |
| `Credit Card Purchase Value` | M10_CC_PURCHASE_VALUE | Value of the Purchase Card procurement.  This value can reflect other charges such as freight. |
| `Credit Card Received at Purchasing Date` | M10_PC_RECVD_PURCHASE_DT |  |
| `Current Issue Count` | M32_CUR_ISS_CNT |  |
| `Current Replenishment Demand` | M32_CUR_REPLEN_DMD |  |
| `Customer Order Charge Code` | M03_CO_CHG_CD |  |
| `Date Code` | M10_DATE_CD |  |
| `Date of Last Action` | X_M10_DOLA | Date type column for M10_DOLA |
| `Delivery Point` | M10_SHOP_DELV_POINT |  |
| `Description Item (Noun Name)` | M32_DESC_ITEM |  |
| `Description Message` | M30_DESC_MSG |  |
| `Detail Drawing Number` | M10_M24_DETAIL_DWG_PIECE_NR |  |
| `Direct Material Inventory Value` | M12_VALUE_DMI |  |
| `Document Created Date` | M10_CREATION_DATE |  |
| `Document Cut Number` | M10_DOC_CUT_NR | Derived column from M10_DOC_CUT_NR ( substr(m10_doc_cut_nr,1,8)). |
| `Document Date` | M10_DOCUMENT_DATE |  |
| `Document Number` | X_M10_DOC_NR |  |
| `Document Status Type` | M14_TYPE_STATUS_CD |  |
| `Document_Created_Date` | M10_CREATION_DATE |  |
| `Drawing Number` | M11_DWG_NR |  |
| `Due Quantity` | M10_QTY_DUE |  |
| `Estimated Shipping Date` | M14_ISS_BLD_NR |  |
| `Expense Account Number` | M03_EXPENSE_ACCOUNT |  |
| `Federal Supply Class` | M30_FSC |  |
| `Foreign Currency Code` | M10_FORGN_CURR_CD | Identifies the foreign currency code. |
| `Fourth Storage Location` | M32_STORAGE_LOCATION_SEC_3 |  |
| `Fund Code` | M11_FUND_CD |  |
| `Hazardous Material Code` | M30_HAZARD_MATL_CD |  |
| `Hull Number` | M02_HULL_NR |  |
| `Inhibit Action Code` | M32_INHIBIT_ACTION_CD |  |
| `Inhibit Replenishment Code` | M32_INHIBIT_REPLHMNT_CD |  |
| `Inspection Code` | X_M10_INSPN_CD | Derived column from M10_DELV_CD_2_5 (substr(m10_delv_cd_2_5,1,1) |
| `Inspection Procedure` | M11_INSPN_PROC |  |
| `Inventory Purge History Count` | M32_INV_PURGE_HSTY_CNT |  |
| `Issue Building Num(a.k.a. ETD)` | M14_ISS_BLD_NR |  |
| `Issue Count Sales` | M32_ISS_CNT_SALES |  |
| `Issue Current Year` | M32_ISS_CUR_YR |  |
| `JML Cumulative Quantity` | M32_QTY_JML_CUM |  |
| `Job Order` | M05_JO_KO |  |
| `Job Order - JO Field` | M05_M04_JO |  |
| `Job Order Charge Code` | M04_JOCHARGECO_CD |  |
| `Job Order Key Operation` | M05_JO_KO |  |
| `Job Order Status Code` | M05_JO_STATUS_CD |  |
| `Job Order Title` | M05_JO_TITLE |  |
| `KO Item Nr` | M11_KO_ITEM_NR |  |
| `Key Event Number` | M05_KEY_EVENT_NR |  |
| `Last Inventory Issue Count` | M32_ISS_CNT_LAST_INV |  |
| `Last Issue Date` | X_M32_DATE_LAST_ISSUE | Date type column for M32_DATE_LAST_ISSUE. |
| `Last Issue Date Julian` | M32_DATE_LAST_ISSUE |  |
| `Last Receipt Date` | X_M32_DATE_LAST_RECEIPT | Date type column for M32_DATE_LAST_ISSUE. |
| `Last Receipt Date Julian` | M32_DATE_LAST_RECEIPT |  |
| `Lead Time Forecast` | M32_LEADTIME_FORECAST |  |
| `Leadtime Demand Deviation` | M32_LEADTIME_DMD_DEVIATION |  |
| `Leadtime Demand Forecast` | M32_LEADTIME_DMD_FORECAST |  |
| `Leadtime Deviation` | M32_LEADTIME_DEVIATION |  |
| `Loc Application Cds` | M32_LOC_APPLICATION_CDS |  |
| `Local Management Code` | M11_LOC_MGT_CD |  |
| `M10_NUC_IND` | M10_NUC_IND |  |
| `M10_XREF_DOC_CUT_NR` | M10_XREF_DOC_CUT_NR |  |
| `M11 Comit Avail Nr` | X_M11_COMIT_AVAIL_NR | Column is derived from character positions 3-5 of the m11_commitment_jo_id |
| `M11_UNIT_IDENT_CD` | M11_UNIT_IDENT_CD |  |
| `M14_ID` | M14_ID |  |
| `M230_COG` | M230_COG |  |
| `M23_M20_FED_SPLY_CODE_FOR_MFRS` | M23_M20_FED_SPLY_CODE_FOR_MFRS |  |
| `M32 Due Quantity` | M32_QTY_DUE |  |
| `M32 Federal Supply Class` | M32_FSC |  |
| `M32 Hazardous Material Code` | M32_HAZARD_MATL_CODE |  |
| `M32 Hold Time` | M32_HOLD_TIME |  |
| `M32 Inspection Code` | M32_INSPN_CD |  |
| `M32 Last Inventory Date` | M32_DATE_LAST_INVENTORY |  |
| `M32 NIIN SMIC` | X_M32_NIIN_SMIC | Derived column from substr(m32_niin_smic_shop_loc,1,11). |
| `M32 Not Ready for Issue Quanity` | M32_QTY_NRFI |  |
| `M32 Ready for Issue` | M32_QTY_RFI |  |
| `M32_COG` | M32_COG |  |
| `M32_SS_LMI_CD` | M32_SS_LMI_CD |  |
| `M32_VALUE_RECEIPTS` | M32_VALUE_RECEIPTS |  |
| `M32_VALUE_SALES` | M32_VALUE_SALES |  |
| `M35_DESCRIPTION_FromDate` | M35_DESCRIPTION_FromDate |  |
| `M35_DESCRIPTION_ToDate` | M35_DESCRIPTION_ToDate |  |
| `M35_INPUT_SEQ_NR` | M35_INPUT_SEQ_NR |  |
| `M35_TECH_DESC` | M35_TECH_DESC |  |
| `MAT Project ID` | M05_JO_KO |  |
| `MSL` | X_M32_SHOP_LOCATION | Derived column from substr(m32_niin_smic_shop_loc,12,3). |
| `Manufacture Part Number` | M10_M37_FSCM_PART_NR |  |
| `Master Date of Last Action` | M05_MSTR_DOLA |  |
| `Material Category Code` | M11_CAT_CD |  |
| `Material Control Code` | M10_MCC_CD |  |
| `Media & Status Code` | M11_MEDIA_STATUS_CD |  |
| `Minimum Order Quantity` | M32_QTY_MINIMUM_ORDER |  |
| `Monthly Demand Forecast` | M32_MTH_DMD_FORECAST |  |
| `Monthly Issue Frequency` | M32_MTH_ISSUE_FREQ |  |
| `Mth Demand Deviation` | M32_MTH_DMD_DEVIATION |  |
| `NIIN SMIC` | M30_NIIN_SMIC |  |
| `NIIN SMIC SS Num & SS Location` | M32_NIIN_SMIC_SHOP_LOC |  |
| `Named: Work Spec` | M10_M31_AVAIL_WORK_ID |  |
| `National Item Identification Number` | X_M30_NIIN | Derived column from substr(M30_NIIN_SMIC,1,9) |
| `Need by Date` | M10_DATE_NEED |  |
| `Need by Date (Julian)` | M10_DATE_NEED |  |
| `Option Key 1` | M10_M36_OPTIONAL_KEY_NR1 |  |
| `Order Quantity` | M32_QTY_ORDER |  |
| `Order Shop` | X_M10_ORDER_SHOP | Derived column from M10_DELV_CD_2_5 (substr(m10_delv_cd_2_5,2,2) |
| `Order Shop Name` | X_M10_ORDER_SHOP | Derived column from M10_DELV_CD_2_5 (substr(m10_delv_cd_2_5,2,2) |
| `Orig Contract ETD Date` | X_M10_DATE_CONTRACT_ETD | Date type column for M10_DATE_CONTRACT_ETD |
| `Original Commitment Value` | M10_VALUE_ORIG_COMIT |  |
| `Original Receipt Date` | X_M10_ORIG_RECEIPT_DATE | Date type column for M10_ORIG_RECEIPT_DATE |
| `PIIN Call Number` | M23_PIIN_CALL_NR |  |
| `Previous Date of Last Action` | M32_PREV_DOLA |  |
| `Previous Job Order ID` | M11_PREVIOUS_JO_ID |  |
| `Primary Storage Location` | M32_STORAGE_LOCATION_PRI |  |
| `Prior INS Code` | M32_PRIOR_INS_CD |  |
| `Priority Code` | M10_PRIORITY_CD |  |
| `Project Code` | M10_PROJ_CD |  |
| `Quantity Issued` | M12_QTY_ISSUED |  |
| `Quantity Not Ready for Issue` | M12_QTY_NRFI |  |
| `Quantity Ready for Issue` | M12_QTY_RFI |  |
| `Quantity Received` | M12_QTY_RECD |  |
| `Quantity Rejected` | M32_QTY_REJ |  |
| `Quantity Status` | M14_QTY_STATUS |  |
| `Receipt Value` | M14_RECEIPT_VALUE | This column is used to record the receipt value for material received.  It is only required for Commitment Code "2" material.  The value is used by th |
| `Received Date` | X_M32_DATE_RECD | Date type column for M32_DATE_RECD. |
| `Received Date Julian` | M32_DATE_RECD |  |
| `Reorder Point Quantity` | M32_QTY_REORDER_POINT |  |
| `Requisition Quantity` | M10_QTY_REQN |  |
| `Routing Identifier` | M32_RI |  |
| `Routing Identifier/Location` | M14_RI_LOC |  |
| `SS Unit Price` | M32_SHOP_STORES_UNIT_PRICE |  |
| `SS Unit of Issue` | M32_UI_SS |  |
| `Secondary Storage Location` | M32_STORAGE_LOCATION_SEC |  |
| `Sequence Number` | M102_SEQ_NR |  |
| `Shelf Life Action Code` | M32_SHELF_LIFE_ACTION_CD |  |
| `Shelf Life Action Code(Non NUC)` | M30_SHELF_LIFE_ACTION_CD |  |
| `Shelf Life Code` | M32_SHELF_LIFE_CD |  |
| `Shelf Life Code(Non NUC)` | M30_SHELF_LIFE_CD |  |
| `Shelf Life Expiration Date` | X_M32_DATE_SHELF_LIFE_EXPIRES | Date type column for M32_DATE_SHELF_LIFE_EXPIRES. |
| `Shelf Life Expiration Date Julian` | M32_DATE_SHELF_LIFE_EXPIRES |  |
| `Ship Project Number` | M02_SHIP_PROJ |  |
| `Special Material ID Code` | X_M30_SMIC | Derived column from substr(M30_NIIN_SMIC,10,2) |
| `Standard Package Quantity` | M32_QTY_STD_PKG |  |
| `Standard Unit of Issue` | M32_UI_STD |  |
| `Status` | M14_STATUS |  |
| `Status Date` | X_M14_DATE_STATUS | Date type column for M14_DATE_STATUS |
| `Status Date Julian` | M14_DATE_STATUS |  |
| `Status Type Code` | M14_TYPE_STATUS_CD |  |
| `Storage In Process Quantity` | M32_QTY_SIP |  |
| `Storage Limit Quantity` | M32_QTY_STORAGE_LIMIT |  |
| `Substitute NIIN SMIC` | M32_SUBSTITUTE_NIIN_SMIC |  |
| `Suffix Code` | M14_MM_SUFFIX_CD |  |
| `Supplemental UIC` | M11_SUPP_UIC_CD |  |
| `Tech Description` | M102_TECH_DESC |  |
| `Third Storage Location` | M32_STORAGE_LOCATION_SEC_2 |  |
| `Type Account Code` | M32_TYPE_ACCT_CD |  |
| `Unit of Issue` | M10_UI |  |
| `Use Code` | X_M10_USE_CD |  |
| `Work Category Code` | X_M05_WORK_CATEGORY | Derived column from M05_JO_KO (SUBSTR(M05_JO_KO,1,2) when first character not = "9",  SUBSTR(M05_JO_KO,5,2) when first characters = "9027", else SUBST |
| `Work Center` | M11_WC |  |
| `Work Status Code` | M05_WORK_STATUS_CD |  |
| `X_M32_DATE_LAST_INVENTORY` | X_M32_DATE_LAST_INVENTORY | Date type column for M32_DATE_LAST_INVENTORY. |
| `X_M32_DOLA` | X_M32_DOLA | Date type column for M32_DOLA. |
| `X_M32_PREV_DOLA` | X_M32_PREV_DOLA | Date type column for M32_PREV_DOLA. |
| `Yearly Replenishment Demand` | M32_REPLEN_DMD_YR |  |

## `MAT_Trigger_Materials.qvd`  (61 fields)

| Qlik field | Source field | Definition |
|------------|--------------|------------|
| `%PTS_TDM_KEY` | ACTIVITY_SA_ID, PTS_TDM_SEQ_ID | Foreign Key value to the TRACKING_DOC_MATERIAL table. |
| `%PTS_TDM_KEY` | ACTIVITY_SA_ID, TDM_SEQ_ID | TDM_SEQ_ID: Primary Key sequence value. |
| `%TDM_TD_Key` | ACTIVITY_SA_ID, TDM_TD_TRACKING_ID | TDM_TD_TRACKING_ID: TRACKING_DOCUMENT Foreign key |
| `%TDM_TD_Key` | ACTIVITY_SA_ID, TD_TRACKING_ID | TD_TRACKING_ID: UNIQUE SEQUENCE NUMBER |
| `%Tracking_Doc_M14_Key` | ACTIVITY_SA_ID, MAT_DOC_CUT_NR, MAT_MM_SUFFIX_CD | MAT_DOC_CUT_NR: MAT Document/Cut number assigned to a tracking system package.  Null if MATERIAL_ID column is populated. |
| `BUILDING_ID` | BUILDING_ID | BUILDING OF THE MCT ITEM |
| `COMMENTS_TX` | COMMENTS_TX | DELIVERY AGENT COMMENTS |
| `CREATION_DT` | CREATION_DT | CREATION DATE AND TIME |
| `DELIVERY_COMPLETION_DT` | DELIVERY_COMPLETION_DT | DATE AND TIME A MANIFEST OR TRIGGER DELIVERY WAS DELIVERED. |
| `DELIVER_TO_BUILDING_ID` | DELIVER_TO_BUILDING_ID | IDENTIFIES THE BUILDING TO DELIVER TO (Old Trigger Delivery M126_SERIAL_NR.M126_DELIVERY_BLD_NR) |
| `DESCRIPTION_TX` | DESCRIPTION_TX | DELIVERY AGENT DESCRIPTION |
| `DESTINATION_ID` | DESTINATION_ID | IDENTIFIES DESTINATION |
| `DOLA_DT` | DOLA_DT | DOLA WITH DATETIME STAMP |
| `FROM_BUILDING_ID` | FROM_BUILDING_ID | Phone number for the point of contact |
| `MANIFEST_NUMBER_ID` | MANIFEST_NUMBER_ID | Manifest number the material was delivered on. |
| `MATERIAL_ID` | MATERIAL_ID | TD_TRACKING_ID for package status, MAT M14_ID for manifest or trigger delivery items, or null when used for MAT material assigned to a package. |
| `MATERIAL_TYPE_CD` | MATERIAL_TYPE_CD | Code identifying the row source of material assigned to a tracking document. M14 identifies a MATERIAL_ID value in the M14_STATUS_REC.M14_ID for a Man |
| `MAT_DOC_CUT_NR` | MAT_DOC_CUT_NR | MAT Document/Cut number assigned to a tracking system package.  Null if MATERIAL_ID column is populated. |
| `MAT_MM_SUFFIX_CD` | MAT_MM_SUFFIX_CD | MAT Suffix for the MAT Document/Cut number assigned to a tracking system package. |
| `PACKAGE_STATUS_TX` | PACKAGE_STATUS_TX | PACKAGE STATUS |
| `PKG_TRK_BADGE_NUMBER_ID` | POC_BADGE_NUMBER_ID | Badge number for the point of contact.  May come from the CUSTOMER table. |
| `PKG_TRK_FIRST_NAME_TX` | POC_FIRST_NAME_TX | First name for the point of contact.  May come from the CUSTOMER table. |
| `PKG_TRK_LAST_NAME_TX` | POC_LAST_NAME_TX | Last name for the point of contact.  May come from the CUSTOMER table. |
| `PKG_TRK_PHONE_NUMBER_TX` | POC_PHONE_NUMBER_TX | Phone number for the point of contact.  May come from the CUSTOMER table. |
| `PKG_TRK_STATUS_FromDate` | PKG_TRK_STATUS_FromDate |  |
| `PKG_TRK_STATUS_ToDate` | PKG_TRK_STATUS_ToDate |  |
| `PKG_TRK_USER_BADGE_NUMBER_ID` | USER_BADGE_NUMBER_ID | BADGE NR OF THE USER'S PACKAGE |
| `POC_BADGE_NUMBER_ID` | POC_BADGE_NUMBER_ID | Badge number for the point of contact |
| `POC_FIRST_NAME_TX` | POC_FIRST_NAME_TX | First name for the point of contact |
| `POC_LAST_NAME_TX` | POC_LAST_NAME_TX | E-mail address for the point of contact. |
| `POC_PHONE_NUMBER_TX` | POC_PHONE_NUMBER_TX | Last name for the point of contact |
| `STATUS_DT` | STATUS_DT | STATUS DATE AND TIME |
| `TDM_CREATION_DT` | TDM_CREATION_DT | Date and time row is inserted |
| `TDM_SEQ_ID` | TDM_SEQ_ID | Primary Key sequence value. |
| `TDM_TD_TRACKING_ID` | TDM_TD_TRACKING_ID | TRACKING_DOCUMENT Foreign key |
| `TD_DELIVERY_LOC` | TD_DELIVERY_LOC | LOCATION |
| `TD_DELIVERY_NAME` | TD_DELIVERY_NAME | FROM M126 DELIVERY NAME |
| `TD_DELIVERY_RDD` | TD_DELIVERY_RDD | RDD |
| `TD_DOC_VALIDATED_CD` | TD_DOC_VALIDATED_CD | A flag used with trigger delivery to identify an item has been valided (sighted). |
| `TD_DOLA_DT` | TD_DOLA_DT | Trigger Delivery date of last action |
| `TD_ISSUED_DT` | TD_ISSUED_DT | TRIGGER DELIVERY ISSUED DATE.  USED DURING TRIGGER DELIVERY CLEANUP. |
| `TD_JO` | TD_JO | FROM M126 JOB ORDER |
| `TD_KO` | TD_KO | FROM M126  KEY OPERATION |
| `TD_LAST_ACTION_CD` | TD_LAST_ACTION_CD | M127 LAST ACTION CD |
| `TD_ORDER_SHOP` | TD_ORDER_SHOP | FROM M126 ORDER SHOP |
| `TD_ORIG_SUFFIX_CD` | TD_ORIG_SUFFIX_CD | Original suffix when a partial trigger is executed |
| `TD_REQ_NAME` | TD_REQ_NAME | FROM M126 REQ NAME |
| `TD_REQ_TEL_NR` | TD_REQ_TEL_NR | FROM M126 REQ TELEPHONE NR |
| `TD_REQ_TYPE` | TD_REQ_TYPE | FROM M126 REQ TYPE |
| `TD_SPECIAL_DELIVERY_INSTR` | TD_SPECIAL_DELIVERY_INSTR | This is Special Delivery Instructions |
| `TD_STORAGE_LOCATION_PRI` | TD_STORAGE_LOCATION_PRI | M127 STORAGE LOCATION PRIM |
| `TD_TRACKING_ID` | TD_TRACKING_ID | UNIQUE SEQUENCE NUMBER |
| `TD_TRIGGER_DELIVERY_GROUP` | TD_TRIGGER_DELIVERY_GROUP | M127 TRIGGER DELIVERY GROUP |
| `TD_USE_CD` | TD_USE_CD | FROM M126 USE CODE |
| `TD_WC` | TD_WC | FROM M126 WORK CENTER |
| `TRACKING_NUMBER_ID` | TRACKING_NUMBER_ID | PACKAGE TRACKING, MANIFEST, OR TRIGGER DELIVERY NUMBER |
| `TRACKING_TYPE_CD` | TRACKING_TYPE_CD | TRACKING TYPE, CAN BE P, M, T, or G |
| `TRIGGER_DELIVERY_NUMBER_ID` | TRIGGER_DELIVERY_NUMBER_ID | Trigger Delivery number the material was triggered on. |
| `URGENT_DELIVERY_CD` | URGENT_DELIVERY_CD | IDENTIFY IF URGENT.  CAN BE Y or N |
| `USER_BADGE_NUMBER_ID` | USER_BADGE_NUMBER_ID | BADGE NUMBER OF PERSON CREATING A MANIFEST |
| `USER_BUILDING_ID` | USER_BUILDING_ID | BUILDING NUMBER OF THE PERSON ENTERING THE STATUS |

---

*Generated from the data dictionary. To regenerate, re-run the inventory generator against*
*`01_sources/qlik/QLIK Data Dictionary.xlsx`.*
