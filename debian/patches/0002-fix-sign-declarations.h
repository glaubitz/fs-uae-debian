Description: Fix sign declarations of multiple integer variables
 fs-uae currently fails to build from source with gcc-6 due to
 some integer variables incorrectly declared as signed. This
 causes a narrowing conversion that can result in information
 loss. This has already fixed upstream but only for the next
 major upstream version which has not been released yet.
 .

--- fs-uae-2.6.2+dfsg.orig/src/include/autoconf.h
+++ fs-uae-2.6.2+dfsg/src/include/autoconf.h
@@ -144,9 +144,9 @@ struct expansionromtype
 	const TCHAR *friendlymanufacturer;
 	DEVICE_INIT init;
 	DEVICE_ADD add;
-	int romtype;
-	int romtype_extra;
-	int parentromtype;
+	uae_u32 romtype;
+	uae_u32 romtype_extra;
+	uae_u32 parentromtype;
 	int zorro;
 	bool singleonly;
 	const struct expansionsubromtype *subtypes;
--- fs-uae-2.6.2+dfsg.orig/src/include/rommgr.h
+++ fs-uae-2.6.2+dfsg/src/include/rommgr.h
@@ -107,7 +107,7 @@ struct romdata {
 	int id;
 	int cpu;
 	int cloanto;
-	int type;
+	uae_u32 type;
 	int group;
 	int title;
 	const TCHAR *partnumber;
