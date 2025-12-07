// --------------------------------------------------------------------------------
//	1文字目：部位
//	a	All	全体
//	b	Back	背景
//	f	Fill	塗り
//	g	Grid	グリッド
//	h	Head	亀頭
//	l	Line	線
//	m	aniMe	アニメ
//	q	-	その他
//	r	Root	根本
//	s	Stem	茎
//	t	poinT	点
//	2文字目：属性
//	a	Angle	角度
//	c	Color	色
//	d	Distance	距離感覚
//	e	Expansion rate	膨張率
//	f	circumFerence	外周
//	h	Height	高さ（未使用）
//	l	Length	長さ
//	p	Permeation rate	濃度
//	r	Radius	半径
//	s	Sec	変形時間
//	v	curVe	カーブ
//	w	Width	太さ
//	x	X	X座標
//	y	Y	Y座標
var clsShapeInkei = clsShapeInkei || {};
clsShapeInkei = {
//20140327
	iMainSt : 0,
	iMainEd : 24,
//	iMainSt : 3,
//	iMainEd : 27,
//20140327
	iDefAx : -150,
	iDefAy : 0,
	iDefAa : 0,
	iMinP0 : 50,	iMaxP0 : 300,	iIvlP0 : 1,	iDefP0 : 140,
	iMinP1 : 50,	iMaxP1 : 300,	iIvlP1 : 1,	iDefP1 : 140,
	iMinP2 : -60,	iMaxP2 : 60,	iIvlP2 : 1,	iDefP2 : 10,
	iMinP3 : -60,	iMaxP3 : 60,	iIvlP3 : 1,	iDefP3 : 10,
	iMinP4 : -40,	iMaxP4 : 40,	iIvlP4 : 1,	iDefP4 : 0,
	iMinP5 : 75,	iMaxP5 : 200,	iIvlP5 : 1,	iDefP5 : 100,
	iMinP6 : 75,	iMaxP6 : 150,	iIvlP6 : 1,	iDefP6 : 100,
	iMinP7 : 0,	iMaxP7 : 1,	iIvlP7 : 1,	iDefP7 : 0,
	iMinP8 : 0,	iMaxP8 : 1,	iIvlP8 : 1,	iDefP8 : 0,
	iMinP9 : 0,	iMaxP9 : 1,	iIvlP9 : 1,	iDefP9 : 0,
	
//20140426
	bJohan : true,
//20140426
//20140404
	bOption0 : true,
	bOption1 : true,
//20140404
	
//20140327
	I_KUKI0 : 0,
	I_KUKI1 : 3,
	I_KITO0 : 6,
	I_KITO1 : 9,
	I_RINKO : 12,
	I_KITO2 : 15,
	I_KITO3 : 18,
	I_KUKI2 : 21,
	I_KUKI3 : 24,
//	I_KUKI0 : 3,
//	I_KUKI1 : 6,
//	I_KITO0 : 9,
//	I_KITO1 : 12,
//	I_RINKO : 15,
//	I_KITO2 : 18,
//	I_KITO3 : 21,
//	I_KUKI2 : 24,
//	I_KUKI3 : 27,
//20140327
	
//20140705
	iStageWidth : 320,
	aiAutoX : [    0,    0,    0,   90,    0],
	aiAutoY : [ -160,  -90,  180,  360,  630],
	aiAutoZ : [    0,    0,    0,    0,    0],
//20140705
	
	iEnd : 0
};

clsShapeInkei.fnGetFny0 = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	return clsShapeInkei.fnGetPath( 90, 80,-20,-40,-30,140, 80,iP7,iP8,iP9);
}

clsShapeInkei.fnGetFny1 = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	return clsShapeInkei.fnGetPath(iP0, 80,  0,  0,  0,iP5,iP6,iP7,iP8,iP9);
}

clsShapeInkei.fnGetFny2 = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	return clsShapeInkei.fnGetPath(iP0,iP1,  0,  0,  0,iP5,iP6,iP7,iP8,iP9);
}

clsShapeInkei.fnGetGtai = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	return clsShapeInkei.fnGetPath(iP0,iP1,  0,  0,iP4,iP5,iP6,iP7,iP8,iP9);
}

clsShapeInkei.fnGetPath = function(iAl,iRf,iSv,iSa,iHa,iSe,iHe,iP7,iP8,iP9) {
	// 定数
//20140327
	var aiX = [0,29,55,84,86,89,91,92,93,96,105,124,129,128,123,116,113,113,111,109,106,103,66,34,0];
	var aiY = [0,2,3,1,2,2,4,2,0,-3,0,1,13,21,29,32,31,31,30,31,32,33,36,35,35];
//	var aiX = [-160,82.32,-33.22,0,29.24,55.29,84.23,86.14,88.79,90.83,91.56,93.48,96.08,105.1,123.52,128.64,128.11,123.26,116.28,113.42,112.51,111.04,109.18,106.4,103.03,66.2,33.87,0,-13.97,24.05,-9.15,-21.98,1.09,-160];
//	var aiY = [-465,-465,-167.9,0,1.39,2.67,0.85,1.32,1.66,3.37,1.24,-0.63,-3.02,-0.56,0.97,12.49,20.36,28.93,31.64,31.03,30.43,29.82,30.51,32.01,33.07,35.89,34.74,35,59.16,77.44,95.25,234.19,496.38,495];
//20140327
	
	var KUKI0 = clsShapeInkei.I_KUKI0;
	var KUKI1 = clsShapeInkei.I_KUKI1;
	var KITO0 = clsShapeInkei.I_KITO0;
	var KITO1 = clsShapeInkei.I_KITO1;
	var RINKO = clsShapeInkei.I_RINKO;
	var KITO2 = clsShapeInkei.I_KITO2;
	var KITO3 = clsShapeInkei.I_KITO3;
	var KUKI2 = clsShapeInkei.I_KUKI2;
	var KUKI3 = clsShapeInkei.I_KUKI3;
	
	// 汎用変数
	var iIdx;
	var iPr;
	var iX;
	var iY;
	var iW;
	var iH;
	var iR;
	var iS;
	var astrTemp = [];
	
	// ----------------------------------------
	// 外周から直径を求める
	var iChokei = iRf / Math.PI;
	
	// 拡大すべき縦幅の倍率を求める
	iPr = (iChokei / (aiY[KUKI3] - aiY[KUKI0]));
	
	// 直径の分だけ縦幅を拡大
	for (iIdx = 0; iIdx < aiX.length; iIdx++) {
		aiY[iIdx] = aiY[iIdx] * iPr;
	}
	
	// 縦幅が拡大した分だけ亀頭の横幅を拡大するが、サオと亀頭の境目のくびれる直前部分がマイナスになる場合は倍率を変更
	if (aiX[RINKO] + (aiX[KUKI1] - aiX[RINKO]) * iPr < aiX[KUKI0] + (aiX[RINKO] - aiX[KUKI0]) * 0.1) {
		iPr = (aiX[KUKI0] + (aiX[RINKO] - aiX[KUKI0]) * 1) / (aiX[RINKO] - aiX[KUKI1]);
	}
	
	// 縦幅が拡大した分だけ亀頭の横幅を拡大する
	for (iIdx = KUKI1; iIdx <= KUKI2; iIdx++) {
		aiX[iIdx] = aiX[RINKO] + (aiX[iIdx] - aiX[RINKO]) * iPr;
	}
	
	// ----------------------------------------
	// サオと亀頭の境目のくびれた直後部分の中心座標Aを求める
	var iX = aiX[KITO0] + (aiX[KITO3] - aiX[KITO0]) * 0.5;
	var iY = aiY[KITO0] + (aiY[KITO3] - aiY[KITO0]) * 0.5;
	
	// 亀頭の縦幅を拡大
	for (iIdx = KITO1 - 1; iIdx <= KITO2 + 1; iIdx++) {
		aiX[iIdx] = iX + (aiX[iIdx] - iX) * (iHe / 100);
		aiY[iIdx] = iY + (aiY[iIdx] - iY) * (iHe / 100);
	}
	
	// ----------------------------------------
	// サオの対角線部分の中心座標Aを求める
	var iX = aiX[KUKI0] + (aiX[KUKI2] - aiX[KUKI0]) * 0.5;
	var iY = aiY[KUKI0] + (aiY[KUKI2] - aiY[KUKI0]) * 0.5;
	
	// サオの縦幅を拡大
	for (iIdx = KUKI0 + 1; iIdx <= KUKI3 - 1; iIdx++) {
		if (iIdx <= KUKI1 - 1 || iIdx >= KUKI2 + 1) {
			aiX[iIdx] = iX + (aiX[iIdx] - iX) * (iSe / 100);
			aiY[iIdx] = iY + (aiY[iIdx] - iY) * (iSe / 100);
		}
	}
	
	// ----------------------------------------
	// 拡大すべき横幅の倍率を求める
	iPr = (iAl / (aiX[RINKO] - aiX[KUKI0]));
	
	// 先端部分のX座標を求める
	iX = aiX[RINKO] * iPr;
	
	// 先端部分の伸び幅を求める
	iW = iX - aiX[RINKO];
	
	// 伸び幅の分だけ亀頭を移動
	for (iIdx = KUKI1; iIdx <= KUKI2; iIdx++) {
		aiX[iIdx] += iW;
	}
	
	// サオの制御点を補正
	for (iIdx = 1; iIdx <= 2; iIdx++) {
		aiX[KUKI0 + iIdx] = aiX[KUKI0] + (aiX[KUKI1] - aiX[KUKI0]) * iIdx / 3;
		aiX[KUKI3 - iIdx] = aiX[KUKI3] + (aiX[KUKI2] - aiX[KUKI3]) * iIdx / 3;
	}
	
	// ----------------------------------------
	// サオの上辺の中心座標Aを求める
	var iX = aiX[KUKI0 + 1] + (aiX[KUKI0 + 2] - aiX[KUKI0 + 1]) * 0.5;
	var iY = aiY[KUKI0 + 1] + (aiY[KUKI0 + 2] - aiY[KUKI0 + 1]) * 0.5;
	
	// 始点から座標Aの半径を求める
	iR = Math.sqrt(Math.pow(iX,2) + Math.pow(iY,2));
	
	// 始点から座標Aの角度を求める
	iS = (Math.atan2(iY,iX) / (Math.PI / 180));
	
	// 角度を変更
	iS -= iSv;
	
	// Yの移動量を求める
	iH = iY - (Math.sin(iS / 180 * Math.PI) * iR);
	
	// 反り
	for (iIdx = KUKI0 + 1; iIdx <= KUKI3 - 1; iIdx++) {
		if (iIdx <= KUKI1 - 1 || iIdx >= KUKI2 + 1) {
			aiY[iIdx] += iH;
		}
	}
	
	// 反った分だけ始点と終点の縦幅を拡大
	var iSvStEdHPer = (1 / Math.cos(iSv / 180 * Math.PI));
	iSvStEdHPer = (iSvStEdHPer - 1) * 0.5 + 1;
	aiY[KUKI0] *= iSvStEdHPer;
	aiY[KUKI3] *= iSvStEdHPer;
	
	// ----------------------------------------
	// サオと亀頭の境目のくびれる直前部分の中心座標Aを求める
	var iX = aiX[KUKI1] + (aiX[KUKI2] - aiX[KUKI1]) * 0.5;
	var iY = aiY[KUKI1] + (aiY[KUKI2] - aiY[KUKI1]) * 0.5;
	
	// 反りの分だけ回転
	for (iIdx = KUKI1; iIdx <= KUKI2; iIdx++) {
		astrTemp = clsShapeInkei.fnRotate(iX,iY,aiX[iIdx],aiY[iIdx],-iSv);
		aiX[iIdx] = astrTemp.iX;
		aiY[iIdx] = astrTemp.iY;
	}
	
	// ----------------------------------------
	// 支点を求める
	var iX = aiX[KUKI0];
	var iY = aiY[KUKI0];
	
	// サオ角度の分だけ回転
	for (iIdx = KUKI0 + 1; iIdx <= KUKI3 - 1; iIdx++) {
		astrTemp = clsShapeInkei.fnRotate(iX,iY,aiX[iIdx],aiY[iIdx],-iSa);
		aiX[iIdx] = astrTemp.iX;
		aiY[iIdx] = astrTemp.iY;
	}
	
	// 曲げた分だけ始点と終点の縦幅を拡大
	var iSaStEdHPer = (1 / Math.cos(iSa / 180 * Math.PI));
	aiY[KUKI0] *= iSaStEdHPer;
	aiY[KUKI3] *= iSaStEdHPer;
	
	// ----------------------------------------
	// サオと亀頭の境目のくびれた直後部分の中心座標Aを求める
	var iX = aiX[KITO1] + (aiX[KITO2] - aiX[KITO1]) * 0.5;
	var iY = aiY[KITO1] + (aiY[KITO2] - aiY[KITO1]) * 0.5;
	
	// 亀頭角度の分だけ回転
	for (iIdx = RINKO - 1; iIdx <= RINKO + 1; iIdx++) {
		astrTemp = clsShapeInkei.fnRotate(iX,iY,aiX[iIdx],aiY[iIdx],-iHa);
		aiX[iIdx] = astrTemp.iX;
		aiY[iIdx] = astrTemp.iY;
	}
	
	// ----------------------------------------
	// 始点と終点の縦幅を求める
	iH = aiY[KUKI3] - aiY[KUKI0];
	
	// 始点が支点の位置で低すぎるため全ての座標を縦幅の半分だけ上に移動する
	for (iIdx = 0; iIdx < aiX.length; iIdx++) {
		aiY[iIdx] -= iH * 0.5;
	}
	
//20140327
//	// Xにマイナスのものがあれば0にする
//	for (iIdx = 0; iIdx < aiX.length; iIdx++) {
//		aiX[iIdx] = aiX[iIdx] < 0 ? 0 : aiX[iIdx];
//	}
//20140327
	
	// ----------------------------------------
	
	return { aiX: aiX, aiY: aiY };
}

clsShapeInkei.fnRotate = function(iBaseX,iBaseY,iX,iY,iAngle) {
	if (iAngle % 360 != 0) {
		// 始点からの半径を求める
		var iR = Math.sqrt(Math.pow(iX - iBaseX,2) + Math.pow(iY - iBaseY,2));
		
		// 始点からの角度を求める
		var iS = (Math.atan2(iY - iBaseY,iX - iBaseX) / (Math.PI / 180));
		
		// 角度を変更
		iS += iAngle;
		
		// 各座標に適用
		iX = iBaseX + Math.cos(iS / 180 * Math.PI) * iR;
		iY = iBaseY + Math.sin(iS / 180 * Math.PI) * iR;
	}
	
	return { iX : iX, iY : iY };
}

clsShapeInkei.fnGetDescList = function(strLang,iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	var strText = '';
	strText += 'Length : ' + iP0 + 'mm<br />';
	strText += 'Diameter : &phi;' + Math.floor(iP1 / Math.PI) + 'mm<br />';
	strText += 'Shaft Curve : ' + iP2 + '&deg;<br />';
	strText += 'Shaft Angle : ' + iP3 + '&deg;<br />';
	strText += 'Glans Angle : ' + iP4 + '&deg;<br />';
	strText += 'Shaft Expansion rate : ' + iP5 + '%<br />';
	strText += 'Glans Expansion rate : ' + iP6 + '%<br />';
	return strText;
}

clsShapeInkei.fnGetDescArray = function(strLang,iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9,asDraw,iW,iH,bDetail) {
	var KUKI0 = clsShapeInkei.I_KUKI0;
	
	var aiX = [];
	var aiY = [];
	var astrText = [];
	var iIdx = -1;
	
	if (bDetail) {
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 11]; aiY[iIdx] = asDraw.aiY[KUKI0 + 11]; astrText[iIdx] = iP0 + 'mm';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 24]; aiY[iIdx] = asDraw.aiY[KUKI0 + 24]; astrText[iIdx] = '&phi;' + Math.floor(iP1 / Math.PI) + 'mm';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 +  1]; aiY[iIdx] = asDraw.aiY[KUKI0 +  3]; astrText[iIdx] = iP2 + '&deg;';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 +  0]; aiY[iIdx] = asDraw.aiY[KUKI0 +  0]; astrText[iIdx] = iP3 + '&deg;';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 13]; aiY[iIdx] = asDraw.aiY[KUKI0 + 13]; astrText[iIdx] = iP4 + '&deg;';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 +  9]; aiY[iIdx] = asDraw.aiY[KUKI0 +  9]; astrText[iIdx] = iP5 + '%';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 23]; aiY[iIdx] = asDraw.aiY[KUKI0 + 23]; astrText[iIdx] = iP6 + '%';
	} else {
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 12]; aiY[iIdx] = asDraw.aiY[KUKI0 + 12]; astrText[iIdx] = iP0 + 'mm';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 1] + (asDraw.aiX[KUKI0 + 23] - asDraw.aiX[KUKI0 + 1]) * 0.5; aiY[iIdx] = asDraw.aiY[KUKI0 + 1] + (asDraw.aiY[KUKI0 + 23] - asDraw.aiY[KUKI0 + 1]) * 0.5; astrText[iIdx] = '&phi;' + Math.floor(iP1 / Math.PI) + 'mm';
	}
	
	return { aiX: aiX, aiY: aiY, astrText: astrText };
}

//20141209
clsShapeInkei.fnConv3d = function(sShape) {
	return clsMorph.fnConvXYtoXYZofCylinder3d(sShape,[clsShapeInkei.iMainSt],[clsShapeInkei.iMainEd],12,[],[0,0]);
}
//20141209

clsShapeInkei.fnGetPath3d = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9,strMode) {
	strMode = strMode || '';
	
	var sShape;
	if (strMode == 'click') {
		sShape = clsShapeInkei.fnGetFny0(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9)
	} else {
		sShape = clsShapeInkei.fnGetPath(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9)
	}
//20141209
//	return clsMorph.fnConvXYtoXYZofCylinder3d(sShape,[0],[24],12,[],[0,0]);
	return clsShapeInkei.fnConv3d(sShape);
//20141209
}

clsShapeInkei.fnMorphDemo3d = function(sShapeSt,sShapeEd,iMorphPer) {
	var sShape = clsMorph.fnGetMophPath3d(sShapeSt,sShapeEd,iMorphPer);
	return sShape;
}

clsShapeInkei.fnOrigMorph3d = function(sShapeSt,sShapeEd,iR) {
}
