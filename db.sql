USE [system_information]
GO
/****** Object:  Table [dbo].[monitor]    Script Date: 10/27/2024 2:44:26 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[monitor](
	[time] [datetime] NULL,
	[cpu_name] [nvarchar](max) NULL,
	[cpu_usage] [numeric](18, 1) NULL,
	[cpu_freq] [numeric](18, 1) NULL,
	[gpu_name] [nvarchar](max) NULL,
	[gpu_memory_total] [numeric](18, 0) NULL,
	[gpu_memory_used] [numeric](18, 0) NULL,
	[gpu_ultilization] [numeric](18, 0) NULL,
	[disk_total] [numeric](18, 2) NULL,
	[disk_used] [numeric](18, 2) NULL,
	[ram_total] [numeric](18, 2) NULL,
	[ram_used] [numeric](18, 2) NULL,
	[net_sent] [numeric](18, 2) NULL,
	[net_received] [numeric](18, 2) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
