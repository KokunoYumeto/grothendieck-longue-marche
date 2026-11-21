#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
void *JxlEncoderCreate(const void *manager) {
    void *(*real)(const void *) = dlsym(RTLD_NEXT, "JxlEncoderCreate");
    void *result=real(manager);
    void (*allow)(void *) = dlsym(RTLD_NEXT, "JxlEncoderAllowExpertOptions");
    if (allow) allow(result);
    return result;
}
int JxlEncoderFrameSettingsSetOption(void *settings, int option, int64_t value) {
    int (*real)(void *, int, int64_t) = dlsym(RTLD_NEXT, "JxlEncoderFrameSettingsSetOption");
    if (option == 0 && getenv("EVIDENCE_JXL_EFFORT")) value=atoi(getenv("EVIDENCE_JXL_EFFORT"));
    return real(settings, option, value);
}
int JxlEncoderAddImageFrame(void *settings, const void *format, const void *buffer, size_t size) {
    int (*real)(void *,const void *,const void *,size_t)=dlsym(RTLD_NEXT,"JxlEncoderAddImageFrame");
    int (*set)(void *,int,int64_t)=dlsym(RTLD_NEXT,"JxlEncoderFrameSettingsSetOption");
    const char *env=getenv("EVIDENCE_JXL_TUNE");
    if(env){ char *copy=strdup(env), *item=strtok(copy,","); while(item){int key;long val;if(sscanf(item,"%d:%ld",&key,&val)==2){int s; if(key==28){int (*setfloat)(void *,int,float)=dlsym(RTLD_NEXT,"JxlEncoderFrameSettingsSetFloatOption");s=setfloat(settings,key,(float)val);}else{s=set(settings,key,val);}if(s)fprintf(stderr,"Tune option %d:%ld returned %d\n",key,val,s);}item=strtok(NULL,",");}free(copy); }
    return real(settings,format,buffer,size);
}
