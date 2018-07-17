#
-include GNUmakefile.local

#
NAME?=		monitoring-t2

#
ifdef PROFILE
export AWS_DEFAULT_PROFILE=${PROFILE}
else
export AWS_DEFAULT_PROFILE=default
endif

ifdef REGION
export AWS_DEFAULT_REGION=${REGION}
else
export AWS_DEFAULT_REGION=us-west-2
endif
