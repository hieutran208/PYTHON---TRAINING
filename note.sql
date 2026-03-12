SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER      PROCEDURE [dbo].[SSM_DLY_TM00_HDTV_KHHANG_D] 
( 
	@tungay	char(8),
	@denngay char(8)
) 
AS 
BEGIN 
	BEGIN /*Thiết lập biến môi trường*/
		SET NOCOUNT ON; --
	END
	
BEGIN /*Khai báo biến*/
		DECLARE @v_Start_Time varchar(32)
		DECLARE @v_End_Time varchar(32)
		DECLARE @v_job varchar(255) 
		DECLARE @v_job_name varchar(255) 
		DECLARE @v_success_value varchar(30) 
		DECLARE @v_error_value varchar(30)
		DECLARE @v_debug_value varchar(30) 
		DECLARE @v_fail_value varchar(30) 
		DECLARE @i_Unit_Code varchar(16) = ''
		DECLARE @i_Param_InPut varchar(256)
		DECLARE @v_Data_Area varchar(256)
		DECLARE @sDLieuThieu varchar(1024) = ''
		DECLARE @sCompletioFlag int
		DECLARE @sDebugFlag int
		DECLARE @sErrorFlag int
		DECLARE @UserName Varchar(60)
		DECLARE @v_ma_NHNN varchar(255) ;
	END

	BEGIN /*Khởi tạo giá trị*/
		SET @v_Start_Time = (SELECT FORMAT(GETDATE(), 'yyyyMMddHHmmss'))
		SET @v_success_value = (SELECT  dbo.fn_GetCompletionStatus())
		SET @sCompletioFlag = (SELECT  dbo.fn_GetCompletionFlag())
		SET @v_error_value =  (SELECT  dbo.fn_GetErrorStatus())
		SET @sErrorFlag = (SELECT  dbo.fn_GetErrorFlag())
		SET @v_debug_value = (SELECT  dbo.fn_GetDebugStatus())
		SET @sDebugFlag = (SELECT  dbo.fn_GetDebugFlag())
		SET @i_Param_InPut = '@i_ngay_du_lieu: ' + @tungay
		SET @v_Data_Area = (SELECT  dbo.fn_GetNgEfundStatus())
		SET @v_job  = OBJECT_NAME(@@PROCID)
		SET @v_job_name = OBJECT_NAME(@@PROCID) + ' '''+@tungay+''' '
		SET @UserName = USER_NAME()
		SET @v_ma_NHNN = (SELECT TOP 1 MA_NHNN FROM BCTK_DON_VI WHERE NGAY_DL = (SELECT MAX(NGAY_DL) FROM BCTK_DON_VI))
	END
	BEGIN TRY 
	/*xu ly store*/
			-- TAO BANG TEMP 
			CREATE TABLE #TM00_HDTV_KHHANG_D (
				MA_QTD varchar(32) NOT NULL,
				MA_DVI varchar(32) NOT NULL,
				ID_HDTD bigint NOT NULL,
				ID_LOAI_HD bigint NOT NULL,
				ID_KHAN_HD bigint NOT NULL,
				ID_KHHANG bigint NOT NULL,
				ID_SPHAM bigint NOT NULL,
				ID_LOAI_LSUAT bigint NOT NULL,
				ID_PTHUC_VAY bigint NOT NULL,
				ID_NGANHKT bigint NOT NULL,
				ID_MDV bigint NOT NULL,
				ID_KHHANG_TVIEN bigint NOT NULL,
				ID_TTE bigint NOT NULL,
				ID_NNO bigint NOT NULL,
				ID_NGUOI_QULY bigint NULL,
				MA_HDTD varchar(64) NOT NULL,
				SO_HDTD varchar(32) NOT NULL,
				MA_KUOC varchar(64) NOT NULL,
				STIEN_VAY decimal(21, 2) NOT NULL,
				SO_TKHOAN varchar(32) NOT NULL,
				NGAY_HD varchar(8) NOT NULL,
				NGAY_GNGAN varchar(8) NOT NULL,
				NGAY_DHAN_HD varchar(8) NOT NULL,
				MOTA_MDV nvarchar(1024) NULL,
				CO_TSDB bit NULL,
				TTHAI varchar(32) NOT NULL,
				NGAY_CNHAT datetime NOT NULL
			)
            --Lấy dữ liệu vào bảng tạm
			BEGIN 
                ;WITH CTE_KHE_UOC AS (
                    SELECT *
                    FROM TMP_A_KHE_UOC A
                    WHERE A.NGAY_DL BETWEEN @tungay AND @denngay
                    AND A.NGAY_DL = ( SELECT MAX(NGAY_DL)
                                      FROM TMP_A_KHE_UOC
                                      WHERE MA_KHE_UOC = A.MA_KHE_UOC
                                      AND NGAY_DL <= @denngay
                                    )
                ),
                CTE_HDTD AS (
                    SELECT *
                    FROM TMP_A_HDTD B
                    WHERE B.NGAY_DL = ( SELECT MAX(NGAY_DL)
                                        FROM TMP_A_HDTD
                                        WHERE MA_HOP_DONG = B.MA_HOP_DONG
                                        AND NGAY_DL <= @denngay
                                      )
                )
				Insert into #TM00_HDTV_KHHANG_D
				SELECT 
                    @v_ma_NHNN AS MA_QTD,
                    A.MA_CHI_NHANH AS MA_DVI,
                    -1 AS ID_HDTD,
                    ISNULL(C.ID, '') AS ID_LOAI_HD,
                    ISNULL(D.ID, '') AS ID_KHAN_HD,
                    ISNULL(E.ID, '') AS ID_KHHANG,
                    ISNULL(F.ID, '') AS ID_SPHAM,
                    -1 AS ID_LOAI_LSUAT,
                    -1 AS ID_PTHUC_VAY,
                    ISNULL(K.ID, '') AS ID_NGANHKT,
                    ISNULL(G.ID, '') AS ID_MDV,
                    ISNULL(M.ID, -1) AS ID_KHHANG_TVIEN,
                    -1 AS ID_TTE,
                    ISNULL(I.ID, '') AS ID_NNO,
                    ISNULL(N.ID, '') AS ID_NGUOI_QULY,
                    B.MA_HOP_DONG AS MA_HDTD,
                    B.SO_HOP_DONG AS SO_HDTD,
                    A.MA_KHE_UOC AS MA_KUOC,
                    B.HAN_MUC_CVAY AS STIEN_VAY,
                    A.SO_TAI_KHOAN AS SO_TKHOAN,
                    B.NGAY_HIEU_LUC AS NGAY_HD,
                    A.NGAY_GIAI_NGAN AS NGAY_GNGAN,
                    B.NGAY_HET_HIEU_LUC AS NGAY_DHAN_HD,
                    B.MO_TA_MUC_DICH_VAY AS MOTA_MDV,
                    CASE WHEN (CASE WHEN B.LOAI_BDAM_TD = 'C' THEN 1 ELSE 0 END) = 1 THEN 1
                         ELSE 0 END AS CO_TSDB,
                    A.TRANG_THAI AS TTHAI,
                    GETDATE() AS NGAY_CNHAT				
				FROM CTE_KHE_UOC A  INNER JOIN CTE_HDTD B 
                                            ON A.MA_HOP_DONG = B.MA_HOP_DONG
                                    INNER JOIN TM00_LOAI_HD_D C 
                                            ON B.MA_LOAI_HOP_DONG = C.MA_LOAI_HD
                                    INNER JOIN TM00_KHAN_D D 
                                            ON D.KY_HAN = B.KY_HAN_VAY 
                                           AND D.MA_DVI_KHAN = B.DVI_KY_HAN
                                    INNER JOIN TM00_KHHANG_D E 
                                            ON E.MA_KHHANG = A.MA_KHACH_HANG
                                    INNER JOIN TM00_SPHAM_CVAY_KHHANG_D F 
                                            ON F.MA_SPHAM = B.MA_SAN_PHAM
                                    INNER JOIN TM00_MDV_CVAY_D G 
                                            ON G.MA_MDV = A.MA_MUC_DICH_VAY
                                    INNER JOIN TM00_NNO_D I 
                                            ON RIGHT(I.MA_NNO,1) = B.NHOM_NO_THEO_TCTD
                                    INNER JOIN TM00_NGANHKT_D K
                                            ON K.MA_NGANHKT=B.MA_NGANH_KT
                                    INNER JOIN TM00_KHHANG_TVIEN_D M 
                                            ON M.MA_TVIEN=B.MA_THANH_VIEN
                                    INNER JOIN TM00_NVIEN_D N 
                                            ON N.USER_ID=B.MA_NGUOI_QLY
			END
		
			--Insert dữ liệu từ bảng tạm và bảng chính
			MERGE INTO TM00_HDTV_KHHANG_D AS TARGET
			USING #TM00_HDTV_KHHANG_D AS SOURCE
			ON TARGET.MA_QTD = SOURCE.MA_QTD AND TARGET.MA_DVI = SOURCE.MA_DVI AND TARGET.MA_KUOC = SOURCE.MA_KUOC
			WHEN MATCHED THEN
				UPDATE SET
					TARGET.ID_HDTD = SOURCE.ID_HDTD,
					TARGET.ID_LOAI_HD = SOURCE.ID_LOAI_HD,
					TARGET.ID_KHAN_HD = SOURCE.ID_KHAN_HD,
					TARGET.ID_KHHANG = SOURCE.ID_KHHANG,
					TARGET.ID_SPHAM = SOURCE.ID_SPHAM,
					TARGET.ID_LOAI_LSUAT = SOURCE.ID_LOAI_LSUAT,
					TARGET.ID_PTHUC_VAY = SOURCE.ID_PTHUC_VAY,
					TARGET.ID_NGANHKT = SOURCE.ID_NGANHKT,
					TARGET.ID_MDV = SOURCE.ID_MDV,
					TARGET.ID_KHHANG_TVIEN = SOURCE.ID_KHHANG_TVIEN,
					TARGET.ID_TTE = SOURCE.ID_TTE,
					TARGET.ID_NNO = SOURCE.ID_NNO,
					TARGET.ID_NGUOI_QULY = SOURCE.ID_NGUOI_QULY,
					TARGET.MA_HDTD = SOURCE.MA_HDTD,
					TARGET.SO_HDTD = SOURCE.SO_HDTD,
					TARGET.STIEN_VAY = SOURCE.STIEN_VAY,
					TARGET.SO_TKHOAN = SOURCE.SO_TKHOAN,
					TARGET.NGAY_HD = SOURCE.NGAY_HD,
					TARGET.NGAY_GNGAN = SOURCE.NGAY_GNGAN,
					TARGET.NGAY_DHAN_HD = SOURCE.NGAY_DHAN_HD,
					TARGET.MOTA_MDV = SOURCE.MOTA_MDV,
					TARGET.CO_TSDB = SOURCE.CO_TSDB,
					TARGET.TTHAI = SOURCE.TTHAI,
					TARGET.NGAY_CNHAT = SOURCE.NGAY_CNHAT
			WHEN NOT MATCHED BY TARGET THEN
				INSERT (MA_QTD,MA_DVI,ID_HDTD,ID_LOAI_HD,ID_KHAN_HD,ID_KHHANG,ID_SPHAM,ID_LOAI_LSUAT,ID_PTHUC_VAY,ID_NGANHKT,ID_MDV,ID_KHHANG_TVIEN,ID_TTE,ID_NNO,ID_NGUOI_QULY,
						 MA_HDTD ,SO_HDTD,MA_KUOC,STIEN_VAY,SO_TKHOAN,NGAY_HD,NGAY_GNGAN,NGAY_DHAN_HD,MOTA_MDV,CO_TSDB,TTHAI,NGAY_CNHAT)
				VALUES (SOURCE.MA_QTD,SOURCE.MA_DVI,SOURCE.ID_HDTD,SOURCE.ID_LOAI_HD,SOURCE.ID_KHAN_HD,SOURCE.ID_KHHANG,SOURCE.ID_SPHAM,SOURCE.ID_LOAI_LSUAT,SOURCE.ID_PTHUC_VAY,SOURCE.ID_NGANHKT,SOURCE.ID_MDV,SOURCE.ID_KHHANG_TVIEN,SOURCE.ID_TTE,SOURCE.ID_NNO,SOURCE.ID_NGUOI_QULY,
						 SOURCE.MA_HDTD ,SOURCE.SO_HDTD,SOURCE.MA_KUOC,SOURCE.STIEN_VAY,SOURCE.SO_TKHOAN,SOURCE.NGAY_HD,SOURCE.NGAY_GNGAN,SOURCE.NGAY_DHAN_HD,SOURCE.MOTA_MDV,SOURCE.CO_TSDB,SOURCE.TTHAI,Getdate());

			--Xoá bảng tạm
			Drop table #TM00_HDTV_KHHANG_D
			
			--Lấy thời gian kết thúc
			SET @v_End_Time = (SELECT FORMAT(GETDATE(), 'yyyyMMddHHmmss'))
			
			--Ghi log hoàn thành
			EXEC sp_Write_Log_ETL @sCompletioFlag ,@tungay,'','',@v_job,@v_job_name,@i_Param_InPut, @v_Data_Area,@v_success_value,'',@v_success_value,@UserName, @v_Start_Time, @v_End_Time
	END TRY  
	BEGIN CATCH  
		SET @v_End_Time = (SELECT FORMAT(GETDATE(), 'yyyyMMddHHmmss'))
		DECLARE @errNumber int = ERROR_NUMBER(),@errState int = ERROR_STATE(), @errSeverity int = ERROR_SEVERITY(), @errLine int = ERROR_LINE(),@errProcedure nvarchar(max) = ERROR_PROCEDURE(), @errMessage nvarchar(max) = ERROR_MESSAGE() 
		EXEC sp_Write_Log_ETL @sErrorFlag,@tungay, '','',@v_job,@errProcedure,@i_Param_InPut, @v_Data_Area,@v_error_value,@errMessage,@v_error_value,@UserName, @v_Start_Time, @v_End_Time
	END CATCH 
END 
GO